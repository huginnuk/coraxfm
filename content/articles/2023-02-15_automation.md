Title: Automation
Date: 2023-02-15
Tags: Software
Summary: Automated Blog Post Workflow

A well known Linkedin influencer crops up in my feed pretty frequently. The influencer often posts screenshots of tweets that they've made. They're not the only one, there are a number of posters that do similar things. I find it interesting becuase Twitter-Linkedin cross posting was a very early integration that I recall.

In fact, if you head over to your [LinkedIn Preferences](https://www.linkedin.com/mypreferences/d/twitter) you can connect Twitter and cross post automatically. I would have thought that most things would want to be cross posted, but then, I'm not an influencer.

I don't like inefficent processes. I dislike the feeling that I'm wasting time. I like automating small things, because it turns a boring action (copy & paste) into an interesting problem to solve (how do I do the thing). With that in mind, I'm going to describe my workflow for publishing a post on this blog. I don't publish very often, but when I do, I don't want to be copying and pasting anything.

I write my blog entries in [Markdown](https://www.markdownguide.org/), essentially, some minimal markup that can easily get converted into HTML. My website is generated in static site generator called [Pelican](https://docs.getpelican.com/en/latest/index.html). I use [git](https://git-scm.com/) for version control, which I self-host with [Gitea](https://gitea.io/en-us/). So far, not much automted. I can't really automate the writing of blog posts.

Now, the automation bits. The Gitea repository syncs every 8 hours with a Github repository. When the Github repository gets the latest code from Gitea, Netlify pulls the website from Gitea. Within the website all the blog posts are included in the [RSS feed](https://www.coraxfm.uk/feed.rss). [Zapier](https://zapier.com) gets the most recent blog post from the RSS feed and does three things: posts on the [CoraxFM Linkedin company page](https://www.linkedin.com/company/coraxfm/), creates a [tweet](https://twitter.com/CoraxFM), and a [Medium story](https://medium.com/@coraxfm).

I think that the trouble with some of the automations is that many people cannot even imagine what can be automated with relative ease. Zapier is a no-code solution to automation. You could replace the version control/static site stuff that here with Wordpress. Or anything else that supports an RSS feed.

What processes might you have to automate?