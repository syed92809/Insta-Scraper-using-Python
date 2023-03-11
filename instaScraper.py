import re

import instaloader

instaScrap=instaloader.Instaloader()
profile=instaloader.Profile.from_username(instaScrap.context, 'cristiano')
print("User Name:", profile.username)
print("User Id:",profile.userid)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
print("Email:",emails)
print("Number of post:",profile.mediacount)
print("Following:",profile.followees)
print("Followers:",profile.followers)
print("URL:",profile.external_url)

# instaScrap.login(user="ahmed03362021",passwd="ahmed..12")
# profile=instaloader.Profile.from_username(instaScrap.context, 'wealth')
# posts=profile.get_posts()
# for index, post in enumerate(posts,1):
#     instaScrap.download_post(post, target=f"{profile.username}_{index}")
