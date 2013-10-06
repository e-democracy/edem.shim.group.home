# coding=utf-8
from gs.group.home.simpletab import PublicTab
from Products.XWFCore.XWFUtils import get_group_by_siteId_and_groupId

class LinksTab(PublicTab):
    def __init__(self, group, request, view, manager):
        PublicTab.__init__(self, group, request, view, manager)
        self.group = group
        
    @property
    def hotTopics(self):
        return self.group.getProperty('hot_topics', [])
    
    @property
    def relatedGroups(self):
        groupLinks = []
        for groupId in self.group.getProperty('related_groups', []):
            group = get_group_by_siteId_and_groupId(self.group,
                                                    self.siteInfo.id,
                                                    groupId)
            gl = u'<a href="%s">%s</a>' % (group.absolute_url(),
                                          group.title_or_id())
            groupLinks.append(gl)
        
        return groupLinks
    
    @property
    def relatedLinks(self):
        return self.group.getProperty('related_links', [])