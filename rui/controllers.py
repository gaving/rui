#!/usr/bin/env python

import urllib
import cgi
import os
import datetime
import time
import urllib

import logging
import cherrypy
import turbogears
import xmlrpclib
import feedparser

from turbogears import controllers, expose, validate, redirect, config, validators
from rui import util
from os.path import *

class Root(controllers.RootController):
    """This class represents the root controller of the application."""

    RTORRENT = xmlrpclib.ServerProxy(turbogears.config.get('rui.rtorrent.rpc', 'http://localhost/RPC2'))
    FEED = turbogears.config.get('rui.feed.url', 'http://localhost/torrents.xml')
    MAX_FEEDS = turbogears.config.get('rui.feed.max_items', 5)
    TORRENT_DIR = turbogears.config.get('rui.feed.download_directory', '/mnt/media/www/torrents')
    log = logging.getLogger(__name__)

    class Torrent:
        """This class represents a torrent"""

        def __init__(self, torrent):
            download = Root.RTORRENT.d

            self.name = download.get_name(torrent)
            self.hash = torrent
            self.size = float(download.get_size_bytes(torrent))
            self.downloaded = float(download.get_bytes_done(torrent))
            self.uploaded = download.get_up_total(torrent)
            self.download_rate = download.get_down_rate(torrent)
            self.upload_rate = download.get_up_rate(torrent)
            self.state = download.get_state(torrent)

            self.image = util.get_mime_image(self.name)
            self.ratio = (self.uploaded / self.size)

        def get_hash(self):
            return self.hash

        def get_name(self):
            return self.name

        def get_downloaded(self):
            return util.format_size(self.downloaded)

        def get_size(self):
            return util.format_size(self.size)

        def get_state(self):
            return self.state

        def get_percentage(self):
            return "%.1f" % ((self.downloaded / self.size) * 100)

        def get_remaining(self):
            return util.format_size((self.size - self.downloaded))

        def get_ratio(self):
            return "%.2f" % self.ratio

        def get_ratio_image(self):
            return util.get_ratio_image(self.ratio)

        def get_status(self):
            return self.status

        def get_uploaded(self):
            return util.format_size(self.uploaded)

        def get_mime_image(self):
            return self.image

        def get_upload_rate(self):
            return util.format_size(self.upload_rate)

        def get_download_rate(self):
            return util.format_size(self.download_rate)

    class Download:
        """This class represents a download"""

        def __init__(self, entry):
            self.name = entry.title
            self.link = entry.link
            self.time = datetime.datetime.fromtimestamp(time.mktime(entry.updated_parsed))
            self.image = util.get_mime_image(self.name)

        def get_link(self):
            return self.link

        def get_mime_image(self):
            return self.image

        def get_encoded_link(self):
            return urllib.quote_plus(self.link)

        def get_encoded_name(self):
            return urllib.quote_plus(self.name)

        def get_short_name(self):
            return util.truncchar(self.name, 8)

        def get_name(self):
            return self.name

        def get_time(self):
            return util.format_size(self.downloaded)

        def get_size(self):
            return util.format_size(self.size)


    @expose(template="rui.templates.index")
    def index(self, **kw):

        torrents = [self.Torrent(torrent) \
                for torrent in Root.RTORRENT.download_list()]

        downloads = [self.Download(entry) \
                for entry in feedparser.parse(Root.FEED).entries]

        folders = ['incoming', 'torrents', 'video', 'tv', 'documentaries']

        return dict(torrents=torrents, downloads=downloads[:Root.MAX_FEEDS],
                folders=folders)

    @expose(format="json")
    @validate(validators = { "file": validators.String()})
    def download(self, file, *args, **kw):
        rtorrent = Root.RTORRENT
        torrent = os.path.join(Root.TORRENT_DIR, "%s%s" % (file, '.torrent'))

        downloaded = False
        if os.path.isfile(torrent):
            try:
                rtorrent.load_start(torrent)
                downloaded = True
                Root.log.debug(os.path.join(Root.TORRENT_DIR, "%s%s" % (file, '.torrent')))
            except Exception, e:
                Root.log.debug(e)
                downloaded = False

        return dict(downloaded=downloaded)

    @expose(format="json")
    @validate(validators = { "hash": validators.String()})
    def erase(self, hash, *args, **kw):
        rtorrent = Root.RTORRENT
        erased = False
        try:
            rtorrent.d.erase(hash)
            erased = True
        except Exception, e:
            Root.log.debug(e)
            erased = False

        return dict(erased=erased)

    @expose(format="json")
    @validate(validators = { "hash": validators.String()})
    def start(self, hash, *args, **kw):
        rtorrent = Root.RTORRENT
        started = False
        try:
            rtorrent.d.start(hash)
            started = True
        except Exception, e:
            Root.log.debug(e)
            started = False

        return dict(started=started)

    @expose(format="json")
    @validate(validators = { "hash": validators.String()})
    def stop(self, hash, *args, **kw):
        rtorrent = Root.RTORRENT
        stopped = False
        try:
            rtorrent.d.stop(hash)
            stopped = True
        except Exception, e:
            Root.log.debug(e)
            stopped = False

        return dict(stopped=stopped)

    @expose()
    def default(self, *args, **kw):
        return "This page is not ready"
