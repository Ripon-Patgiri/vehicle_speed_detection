from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["car in road", 'single vehicle portrait picture']

for key in keywords:
    response().download(key, 50)
