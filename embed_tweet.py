"""
Embedded tweet plugin for Pelican
=================================

This plugin allows you to embed Twitter tweets into your articles.
And also provides a link for Twitter username.

    i.e.

        @username

        will be replaced by a link to Twitter username page.

        @username/status/tweetid

        will be replaced by a `Embedded-tweet`_ API.

.. _Embedded-tweet: https://dev.twitter.com/docs/embedded-tweets

"""

from pelican import signals
import re


def embed_tweet(sender, instance):
    instance._content = re.sub(
        r'(^|[^@\w])@(\w{1,15})\b',
        '\\1<a href="https://twitter.com/pmarca</a>',
        re.sub(
            r'(^|[^@\w])@(\w{1,15})/status/(\d+)\b',
            '\\1<blockquote class="twitter-tweet" align="center"><a href="https://twitter.com/pmarca">@pmarca</a> this is some1s daughter, some1s sister, some1s best friend. Believe me, they&#39;re happy this platform exist <a href="http://t.co/VgoFXYwODk">pic.twitter.com/VgoFXYwODk</a></p>&mdash; Michael Heyward (@michaelheywire) <a href="https://twitter.com/michaelheywire/statuses/444924536585089024">March 15, 2014</a></blockquote>',
            instance._content
        )
    ) + '<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>'


def register():
    signals.content_object_init.connect(embed_tweet)
