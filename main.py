import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import pandas as pd
import praw
from praw.models import MoreComments

reddit = praw.Reddit(user_agent="Comment Extraction (by /u/LeafedOak70)",
                     client_id="g50qqyXA_Y0Ed8hPmueMbw", client_secret="ei8ho_5pJW4c0oWPAo2yP-VehDLKaw")
# url = "https://www.reddit.com/r/AskReddit/comments/4lmm61/what_is_a_fun_fact_that_always_blows_peoples_minds/"
# url = "https://www.reddit.com/r/AskReddit/comments/qk3hec/whats_a_cool_fact_you_think_others_should_know/"
# url = "https://www.reddit.com/r/AskReddit/comments/1rsyio/whats_your_favorite_fun_fact/"
url = "https://www.reddit.com/r/AskReddit/comments/j6m73/what_are_the_best_random_facts_you_know_reddit/"
submission = reddit.submission(url=url)


posts = []
for top_level_comment in submission.comments[1:]:
    if isinstance(top_level_comment, MoreComments):
        continue
    comment = top_level_comment.body
    
    length = len(comment)
    if length < 300:
        posts.append(comment)
print(posts)
print("Found %d comments"%len(posts))
driver = webdriver.Firefox()
for messeges in posts:
    driver.get("https://secretm.me/message.php?id=4xa468ue")
    messegeBox = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[1]/textarea")
    messegeBox.clear()
    messegeBox.send_keys(messeges)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/form/input[2]").click() 
driver.close()