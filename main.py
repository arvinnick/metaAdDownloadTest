from AdDownloader import adlib_api
from AdDownloader.media_download import start_media_download

access_token = input("access token:")

plt_ads_api = adlib_api.AdLibAPI(access_token, project_name="test2")


plt_ads_api.add_parameters(ad_reached_countries = 'US', ad_delivery_date_min = "2020-10-01", ad_delivery_date_max = "2020-10-03",
                           ad_type = "POLITICAL_AND_ISSUE_ADS", search_page_ids = "us_parties.xlsx")

plt_ads_api.get_parameters()
plt_data = plt_ads_api.start_download()

start_media_download(project_name = "test2", nr_ads = 20, data = plt_data)
