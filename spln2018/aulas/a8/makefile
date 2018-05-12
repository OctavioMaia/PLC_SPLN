rss='http://feeds.feedburner.com/PublicoRSS?format=xml'
hoje=$(shell date '+%m-%d')
xpath=//div[@id="story-content"]
$(hoje).rss:
	wget $(rss) -O $(hoje).rss
$(hoje).urls: $(hoje).rss
	xidel $(hoje).rss -e //item/link > $(hoje).urls
$(hoje).files: $(hoje).urls
	mkdir -p $(hoje)
	cd $(hoje); wget -i ../$(hoje).urls
	ls $(hoje) > $(hoje).files
p4: $(hoje).files
	mkdir -p noticias
	cd $(hoje) ; for a in *; do xidel $$a -e '$(xpath)' --xml > ../noticias/$(hoje)-$$a.xml; done
