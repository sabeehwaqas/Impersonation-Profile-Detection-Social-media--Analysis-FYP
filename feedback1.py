import os
import cv2
from PIL import Image
import face_recognition
from skimage import io,measure
from PIL import Image
import glob
import tensorflow as tf
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
# from keras.preprocessing import image
import keras.utils as image
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
import keras.utils as image
from keras.models import Model
import numpy as np



def find_cluster_id(user_twitter_search, user_osint):
    matched = []
    osint_dir = rf'C:\Users\Dell\OneDrive\Desktop\Osint\{user_osint}'
    results_dir = rf'C:\Users\Dell\OneDrive\Desktop\{user_twitter_search}\results'
    flag = 0


    for i in range(1,3):
        check_for_designation = 0
        imagee = f'{user_osint}{i}'+'.png'
        known_path = os.path.join(osint_dir,imagee)
        print(known_path)
        try:
            known_image = face_recognition.load_image_file(known_path)
            known_encoding = face_recognition.face_encodings(known_image)[0]
        except Exception as e:
            print(known_path, "does not have face")
            check_for_designation = 1
        if check_for_designation == 0:
            for i in range(1,100):
                result_dir1 = results_dir + "\\" + f"cluster_{i}"
                if not os.path.exists(result_dir1):
                    print("moving to another image")
                    flag = 1
                    break
                filenames = os.listdir(result_dir1)

                for files in filenames:
                    directroy = os.path.join(result_dir1,files)
                    unknown_image = face_recognition.load_image_file(directroy)
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
                    #print(directroy)
                    #print(results)

                    if results == [True]:
                        if result_dir1 not in matched:
                            matched.append(result_dir1)
    return matched
            #os.pathjoin(result_dir1,)
            #unknown_image = face_recognition.load_image_file()


#duplicate_images(r'C:\Users\Dell\OneDrive\Desktop\imran khan\similarity\@imrankhanpti.png', 'imran khan')

def affiliated_images_for_feature_matching(user_twitter_search, user_osint):

    osint_dir = fr'C:\Users\Dell\OneDrive\Desktop\Osint\{user_osint}'
    similarity_dir = fr'C:\Users\Dell\OneDrive\Desktop\{user_twitter_search}\similarity'
    filenames_1 = os.listdir(osint_dir)
    filenames_2 = os.listdir(similarity_dir)
    affiliation_file_name = []
    matched = []
    for files1 in filenames_1:

        dir = os.path.join(osint_dir,files1)
        try:
            known_image = face_recognition.load_image_file(dir)
            known_encoding = face_recognition.face_encodings(known_image)[0]
        except Exception as e:
            affiliation_file_name.append(files1)

    for files in affiliation_file_name:
        dir1 = os.path.join(osint_dir,files)
        for files2 in filenames_2:
            dir2 = os.path.join(similarity_dir,files2)
            img1 = cv2.imread(dir1, cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imread(dir2, cv2.IMREAD_GRAYSCALE)
            sift = cv2.xfeatures2d.SIFT_create()
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)
            good_matches = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                     good_matches.append(m)

            if len(good_matches)>18:
                matched.append(files2)

    return matched


def image_detect(user_twitter_search, user_osint):

    osint_dir = fr'C:\Users\Dell\OneDrive\Desktop\Osint\{user_osint}'
    similarity_dir = fr'C:\Users\Dell\OneDrive\Desktop\{user_twitter_search}\similarity'
    matched = []
    # Load the VGG16 model
    base_model = VGG16(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)
    filenames_osint = os.listdir(osint_dir)
    filenames_similarity = os.listdir(similarity_dir)
    for files_osint in filenames_osint:
        img1_path = os.path.join(osint_dir,files_osint)
        for files_similarity in filenames_similarity:
            img2_path = os.path.join(similarity_dir,files_similarity)
            img1 = image.load_img(img1_path, target_size=(224, 224))
            img2 = image.load_img(img2_path, target_size=(224, 224))

            # Preprocess the images
            x1 = image.img_to_array(img1)
            x1 = np.expand_dims(x1, axis=0)
            x1 = preprocess_input(x1)

            x2 = image.img_to_array(img2)
            x2 = np.expand_dims(x2, axis=0)
            x2 = preprocess_input(x2)

            # Extract features from the images
            features1 = model.predict(x1)
            features2 = model.predict(x2)

            # Compare the features
            similarity = np.dot(features1, features2.T) / (np.linalg.norm(features1) * np.linalg.norm(features2))
            if similarity >=0.54:
                print(similarity)
                print(files_similarity)
                print(files_osint)

                matched.append(files_similarity)
    #print(files_similarity)
    return matched

def image_detect_duplicates(twitter_id, user_twitter_search):
    from keras.applications.vgg16 import VGG16, preprocess_input
    from keras.preprocessing import image
    import keras.utils as image
    from keras.models import Model
    import numpy as np
    duplicates = []
    similarity_dir = fr'C:\Users\Dell\OneDrive\Desktop\{user_twitter_search}\similarity'

    # Load the VGG16 model
    base_model = VGG16(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)
    filenames_similarity = os.listdir(similarity_dir)
    for i in range(1,2):
        img1_path = os.path.join(similarity_dir,twitter_id+ '.png')
        for files_similarity in filenames_similarity:
            img2_path = os.path.join(similarity_dir,files_similarity)
            img1 = image.load_img(img1_path, target_size=(224, 224))
            img2 = image.load_img(img2_path, target_size=(224, 224))

            # Preprocess the images
            x1 = image.img_to_array(img1)
            x1 = np.expand_dims(x1, axis=0)
            x1 = preprocess_input(x1)

            x2 = image.img_to_array(img2)
            x2 = np.expand_dims(x2, axis=0)
            x2 = preprocess_input(x2)

            # Extract features from the images
            features1 = model.predict(x1)
            features2 = model.predict(x2)

            # Compare the features
            similarity = np.dot(features1, features2.T) / (np.linalg.norm(features1) * np.linalg.norm(features2))

            if similarity >0.7:

                duplicates.append(files_similarity)

    return duplicates



'''

twitter_search_query = 'travis scott'
osint_search_query = 'Travis Scott'
twitter_id = '@trvisxx'

'''

#---------------------------------find_cluster_id--------------------------------------------------------#
#find_cluster_id(user_twitter_search=twitter_search_query,user_osint=osint_search_query)



#---------------------------------check_if_images_are_duplicates_with_in_similarity-----------------------------------------#
#image_detect_duplicates(twitter_id,twitter_search_query)


#---------------------------------check_for_feature_extraction_for_-----------------------------------------------------------------------#
#matched_list_2 = affiliated_images_for_feature_matching(user_twitter_search=twitter_search_query,user_osint=osint_search_query)

#----------------------------------detect_if_same_objects_in_2_images_for_osint_feedback-------------------------------------------#
#image_detect(user_twitter_search=twitter_search_query,user_osint=osint_search_query)