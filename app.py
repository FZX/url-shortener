#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import gevent.monkey
gevent.monkey.patch_all()
from datetime import datetime
from validators import url as urlcheck
from sqlalchemy import (Table, Column, Integer, String, DateTime, ForeignKey,
                        Boolean, create_engine, Sequence, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, relationship

from bottle import (route, template, static_file, request, response, error,
                    install, redirect, run)
from bottle.ext.sqlalchemy import Plugin


Base = declarative_base()
engine = create_engine("sqlite:///./sqlitedb/linksdb.db")

plugin = Plugin(engine, Base.metadata, keyword="db", create=True)
install(plugin)

Session = sessionmaker(bind=engine)
session = Session()

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer(), Sequence("links_id_seq"), primary_key=True)
    link = Column(String(1000))
    clicks = Column(Integer(), default=0)
    created_on = Column(DateTime(), default=datetime.now)

# Base.metadata.create_all(engine)

site = "http://localhost:8080"

def short(link):
    """If your your link base
    will hit more then 100k
    check this one http://stackoverflow.com/a/742047
    """
    link_in_db = session.query(Link).filter(Link.link == link).first()
    if link_in_db:
        return link_in_db.id
    else:
        shorted_to_db = Link(link=link)
        session.add(shorted_to_db)
        session.commit()
        return shorted_to_db.id

def count_links():
    """Total shrinked links.

    func.count will return total number of
    shrinked links in database.
    """
    link_count = session.query(func.count(Link.id)).first()[0]
    return link_count


@route("/")
def index(db):
    """Main route.

    Here we returning index template
    variable site assigned with global site.
    variable total is getting value from count_links()
    function.
    """
    return template("./views/index.html", site=site, total=count_links())

@route("/<id:int>/stats")
def stats(db, id):
    """Stats route.

    Getting stats of current link with passed id.
    variable id. That id user passes.
    url=url.link Url wich was shrinked.
    click=url.clicks how many times was used shrinked url.
    """
    url = db.query(Link).filter(Link.id == id).first()
    if url:
        return template("./views/stats.html", id=id, url=url.link,
                        clicks=url.clicks, created=url.created_on,
                        site=site, total=count_links())
    else:
        redirect("/")

@route("/<id:int>")
def redir(db, id):
    """Redirect route.

    Here we are redirecting to actual url.
    Checking the id into database. If we have row
    with that id into database we are increasing
    clicks value by 1 and redirecting to actual url.
    Else we are redirecting to our mainpage.
    """
    url = db.query(Link).filter(Link.id == id).first()
    if url:
        url.clicks += 1
        db.commit()
        redirect(url.link)
    else:
        redirect("/")


@route("/api", method="POST")
def api():
    """API

    Getting url via Post method.
    if url is missing http we are adding it.
    Also we are checking if url is valid with validators
    package. After that we are calling short() function.
    Route will return json object.
    """
    url = request.forms.link
    if url:
        if not url.startswith("http"):
            url = "http://" + url
        if not urlcheck(url):
            return {"status": "error"}
        shorted = site + "/" + str(short(url))
        return {"status": "success", "url": shorted}
    else:
        return {"status": "error"}

@route("/storage/<filename:path>")
def files(filename):
    """Returning static files

    """
    return static_file(filename, root="./views/static")



if __name__ == "__main__":
    run(host="localhost", port="8080", server="gevent",
        debug=True, reloader=True)
