ARTICLE_HTML_TEMPLATE= '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Website</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <nav class="navbar background">
            <ul class="nav-list">
                <div class="logo">
                    <a href="index.html">
                    <img src= "Henry.png">
                </div>
                <li><a href="articlepage.html">Articles</a></li>
            </ul>
        </nav>

        <p>The title of this article is:
        {article_title}
        </p>

    </body>

    </html>
'''
