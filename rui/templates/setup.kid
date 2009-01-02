<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en-GB" xmlns:py="http://purl.org/kid/ns#">
    <head>
        <meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />
        <title>rui - setup</title>
        <link rel="shortcut icon" href="favicon.ico" />
        <link rel="icon" href="favicon.ico" />
        <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
    </head>
    <body>

    <div id="header">
        <h1>setup</h1>
    </div>

    <div id="main">
        <div py:if="tg_flash" class="flash" py:content="tg_flash"></div>

        <fieldset>
            <h5>general</h5>
            <p>general stuff</p>
            <form method="post" action="/index" onsubmit="return validateOnSubmit();">
                <p>
                <label for="host">host:</label>
                <input id="host" type="text" class="inputField" name="host" value="${host}" />
                </p>
                <p>&nbsp;&nbsp;</p>
                <p>
                <input type="submit" class="inputField" name="submit" value="apply changes" />
                </p>
            </form>
        </fieldset>
        </div>
</body>
</html>
