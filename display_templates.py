# display_templates.py

# Template for displaying a post title

title_temp = """
# <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
# <h4 style="color:white;text-align:center;">{}</h4>
# <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
# <h6>Author: {}</h6>
# <br/>
# <br/>
# <p style="text-align:justify"> {}</p>
# </div>
# """

# Template for displaying a full post
post_temp = """
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<h6>Author: {}</h6>
<h6>Date: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;">
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""