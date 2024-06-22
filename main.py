from AdDownloader import adlib_api
from AdDownloader.media_download import start_media_download

with open("./token") as f:
    access_token = f.read()

ads_api = adlib_api.AdLibAPI(access_token, project_name="test2", version="v20.0")
ads_api.add_parameters(ad_reached_countries='DE', language='en', search_terms="'",
                       ad_delivery_date_min='2024-06-01', ad_delivery_date_max='2024-06-19', media_type="IMAGE")

params = ads_api.get_parameters()
data = ads_api.start_download(params)
# data.to_csv("./download.csv", index=False)
# start_media_download(project_name="test2", nr_ads = 20, data=data)
