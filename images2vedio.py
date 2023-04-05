# import cv2
# import os
#
# def images_to_video(img_folder, output_video, fps):
#     # 获取图片文件夹中的所有图片
#     images = [img for img in os.listdir(img_folder) if img.endswith(".png") or img.endswith(".jpg") or img.endswith(".jpeg")]
#
#     # 按文件名排序，确保图像按正确的顺序加载
#     images.sort()
#
#     # 读取第一张图片以获取图像尺寸
#     frame = cv2.imread(os.path.join(img_folder, images[0]))
#     height, width, _ = frame.shape
#
#     # 定义视频编写器，设置输出视频名，编解码器，帧速率和帧大小
#     video_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
#
#     # 将图片逐帧添加到视频
#     for image in images:
#         video_writer.write(cv2.imread(os.path.join(img_folder, image)))
#
#     # 释放视频编写器
#     video_writer.release()
#
# # 设置图像文件夹路径，输出视频文件名，帧速率
# image_folder = 'Images2video'
# output_video = 'output_video.mp4'
# fps = 20
#
# # 将图片转换为视频
# images_to_video(image_folder, output_video, fps)

