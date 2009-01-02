<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en-GB" xmlns:py="http://purl.org/kid/ns#">
    <head>
        <meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />
        <title>sokar</title>
        <link rel="shortcut icon" href="favicon.ico" />
        <link rel="icon" href="favicon.ico" />
        <link rel="stylesheet" type="text/css" href="static/styles.css" />
        <script type="text/javascript" src="static/js/sorttable.js"></script>
        <script type="text/javascript" src="static/js/jquery.js"></script>
        <script type="text/javascript" src="static/js/jquery.contextmenu.js"></script>
        <script type="text/javascript" src="static/js/js.js"></script>
    </head>
    <body>
        <div id="header">
            <div id="button-bar" style="float: right">
                <img id="add-button" src="static/images/add.png" />
                <input id="add-input" type="text" size="40" />
            </div>
            <h1>torrents</h1>
        </div>
        <div id="main">
            <div class="contextMenu" id="torrentContext">
                <ul>
                    <li id="open"><img src="static/images/open.png" /> Open</li>
                    <li id="start"><img src="static/images/start.png" /> Start</li>
                    <li id="stop"><img src="static/images/stop.png" /> Stop</li>
                    <li id="delete"><img src="static/images/delete.png" /> Delete</li>
                </ul>
            </div>
            <table class="main sortable">
                <thead>
                    <tr class="head">
                        <th></th>
                        <th>filename</th>
                        <th>progress</th>
                        <th>size</th>
                        <th>remaining</th>
                        <th>downloaded</th>
                        <th>uploaded</th>
                        <th>down</th>
                        <th>up</th>
                        <th>ratio</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr py:for="torrent in torrents" class="menu ${('stopped','active')[ torrent.get_state() == 1 ]}" hash="${torrent.get_hash()}" state="${torrent.get_state()}">
                        <td><img src="static/images/icons/${torrent.get_mime_image()}" /></td>
                        <td><a href="/info/${torrent.get_hash()}">${torrent.get_name()}</a></td>
                        <td>
                            <div class="prog-border">
                                <div class="prog-bar" style="width: ${torrent.get_percentage()}%;">
                                    <div style="font: 7pt Tahoma, sans-serif; text-align:
                                            right;">${torrent.get_percentage()}%</div>
                                </div>
                            </div>
                        </td>
                        <td>${torrent.get_size()}</td>
                        <td>${torrent.get_remaining()}</td>
                        <td>${torrent.get_downloaded()}</td>
                        <td>${torrent.get_uploaded()}</td>
                        <td>${torrent.get_download_rate()}/s</td>
                        <td>${torrent.get_upload_rate()}/s</td>
                        <td title="${torrent.get_ratio()}"><img src="static/images/icons/${torrent.get_ratio_image()}" /></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div id="footer">
            <div class="column">
                <div class="section">
                    <h3>FOLDERS</h3>
                    <ul py:for="folder in folders">
                        <li style="list-style-image: url(static/images/icons/folder.png)">
                            <a href="">${folder}</a></li>
                    </ul>
                </div>
            </div>
            <div class="column" style="width: 50%" id='feed'>
                <div class="section">
                    <h3>RSS FEED</h3>
                    <ul py:for="download in downloads">
                        <li style="list-style-image: url(static/images/icons/${download.get_mime_image()})">
                            <a href="/download/${download.get_name()}">${download.get_name()}</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
</html>
