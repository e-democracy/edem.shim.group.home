# coding=utf-8
from gs.group.member.viewlet import GroupAdminViewlet


class AboutTab(GroupAdminViewlet):
    
    def __init__(self, group, request, page, manager):
        super(AboutTab, self).__init__(group, request, page, manager)

    @property
    def show(self):
        return True

    @property
    def aboutText(self):
        return getattr(self.context, 'aboutText', '')

    @property
    def facebookId(self):
        return getattr(self.context, 'facebookId', '')

    @property
    def twitterId(self):
        return getattr(self.context, 'twitterId', '')
