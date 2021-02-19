# -*- coding: utf-8 -*-

from Products.CMFPlone.browser.search import Search


class PocSearch(Search):
    valid_keys = ('sort_on', 'sort_order', 'sort_limit', 'fq', 'fl', 'facet', "core")

    def results(self):
        results_base = super(PocSearch, self).results()
        return results_base
