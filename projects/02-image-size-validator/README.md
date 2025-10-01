## multipart/formdata

This is a content type used when you submit forms with files via HTTP.

Example:
When you upload a profile picture on a website, the form sends data like this:

Content-Type: multipart/form-data

It allows sending:
Text fields (name=John)
Files (photo.jpg, resume.pdf)