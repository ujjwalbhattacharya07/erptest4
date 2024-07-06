portal = context.getPortalObject()
howto_dict = context.Zuite_getHowToInfo()

# remove the currency if it was created by us before
currency = context.portal_catalog.getResultValue(portal_type='Currency',
                                                 title=howto_dict['create_event_howto_currency_title'],
                                                 local_roles='Owner',)
if currency is not None:
  context.currency_module.deleteContent(currency.getId())

# remove the person of the test if existing
person_list = context.Zuite_checkPortalCatalog(portal_type='Person', max_count=1,
                                               title=howto_dict['create_event_howto_person_title'])
if person_list is not None:
  portal.person_module.deleteContent(person_list[0].getId())

# remove the person of the test if existing
person_list = context.Zuite_checkPortalCatalog(portal_type='Person', max_count=1,
                                               title=howto_dict['create_event_howto_person2_title'])
if person_list is not None:
  portal.person_module.deleteContent(person_list[0].getId())

# remove the organisation of the test if existing
organisation_list = context.Zuite_checkPortalCatalog(portal_type='Organisation', max_count=1,
                                                     title=howto_dict['create_event_howto_organisation_title'])
if organisation_list is not None:
  portal.organisation_module.deleteContent(organisation_list[0].getId())

# remove the campaign if exist
campaign_list = context.Zuite_checkPortalCatalog(portal_type='Campaign', max_count=1,
                                                 title=howto_dict['create_event_howto_campaign_title'])
if campaign_list is not None:
  portal.campaign_module.deleteContent(campaign_list[0].getId())

# remove the event if exist
event_list = context.Zuite_checkPortalCatalog(portal_type='Mail Message', max_count=999,
                                              title=howto_dict['create_event_howto_event_title'])
if event_list is not None:
  portal.event_module.deleteContent([event.getId() for event in event_list])

#remove the preference of the test if existing
pref = getattr(context.portal_preferences, howto_dict['howto_preference_id'], None)

if pref is not None:
  context.portal_preferences.deleteContent(howto_dict['howto_preference_id'])

return "Clean Ok"
