import streamlit as st

import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os.path as osp
import glob


from PIL import Image
import requests
import pandas as pd
from io import BytesIO


# authentification
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')

    page = st.sidebar.selectbox("探索或预测", ("list_of_food",
        "about_one_food"
        ))

    if page == "list_of_food":

        st.title("食物食谱")
        st.write("Rapid API[link](https://rapidapi.com/rapihub-rapihub-default/api/chinese-food-db)")


            # st.text(generated_text)

        # urll =  st.text_input("域名, eg facebook.com", value="taobao.com")
        # if st.button("发送"):
            # url = "https://website-contacts-scraper.p.rapidapi.com/scrape-contacts"

            # querystring = {"query":urll}

            # headers = {
            #     "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            #     "X-RapidAPI-Host": "website-contacts-scraper.p.rapidapi.com"
            # }

            # response = requests.request("GET", url, headers=headers, params=querystring)
            # ini_string_s = response.json()
            # print(ini_string_s)
            # for s in ini_string_s["data"][0]["emails"]:
            #     st.text(s["value"])
            #     st.text("源: ")
            #     st.text(s["sources"])
            #     st.text("")
            #     st.text("")


            # st.text(ini_string_s)
        url = "https://chinese-food-db.p.rapidapi.com/"

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "chinese-food-db.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
          # response_s = requests.request("GET", url_s, headers=headers, params=querystring)
        ini_string_s = response.json()
        # df_p = pd.DataFrame.from_dict(ini_string_s, orient='columns')
        for x in ini_string_s:
            st.text(x["id"])
            st.text(x["title"])
            # if x["difficulty"] == "Easy":
            st.text(x["difficulty"])
            # elif x["difficulty"] == "Medium":
            # elifx["difficulty"] == "Easy":
            response = requests.get(x["image"])
            img = Image.open(BytesIO(response.content))
            st.image(img)
            st.text("")

        # st.table(df_p)

        # print(response.text)


    else:
        st.title("食物食谱")
        pp1=st.slider("id",0,200,1)
        url = "https://chinese-food-db.p.rapidapi.com/"+str(pp1)

        headers = {
            "X-RapidAPI-Key": "bd10c657b4msh6dbd4f9bf219b22p14f68ajsn0d507d4fae87",
            "X-RapidAPI-Host": "chinese-food-db.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        ini_string_s = response.json()

        st.text(ini_string_s["id"])
        st.text(ini_string_s["title"])
        st.text(ini_string_s["difficulty"])
        st.text(ini_string_s["portion"])
        st.text(ini_string_s["time"])
        st.text(ini_string_s["description"])

        st.text("")
        st.text("ingredients")
        for f in ini_string_s["ingredients"]:
            st.text(f)

        st.text("")
        st.text("method")
        df_p = pd.DataFrame.from_dict(ini_string_s["method"], orient='columns')
        st.table(df_p)
        response = requests.get(ini_string_s["image"])
        img = Image.open(BytesIO(response.content))
        st.image(img)




    # page = st.sidebar.selectbox("探索或预测", ("将图像放大为高清",
    #     "肺炎x_ray图像分类", 
    #     "生成动漫人脸图像"
    #     ))

    # if page == "肺炎x_ray图像分类":
    #     st.title("使用谷歌的可教机器进行图像分类")
    #     st.write("Google Teachable machine"" [link](https://teachablemachine.withgoogle.com/train/image)")
    #     st.header("肺炎x_ray")
    #     st.text("上传肺x_ray图片")

    #     uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
    #     if uploaded_file is not None:
    #         image = Image.open(uploaded_file).convert('RGB')
    #         st.image(image, caption='上传了图片。', use_column_width=True)
    #         st.write("")
    #         st.write("分类...")
    #         label = teachable_machine_classification(image, 'pneumonia__x_ray_image_classify_normal_vs_penumonia.h5')
    #         if label == 0:
    #             st.write("正常")
    #         else:
    #             st.write("肺炎")

    #     st.text("类:正常,肺炎")

    #     # 0 normal
    #     # 1 pneumonia
    # elif page =="将图像放大为高清":
    #     st.title("使用 ESGAN 放大图像")
    #     st.write("ESGAN 安装"" [link](https://github.com/xinntao/ESRGAN)")
    #     st.write("ESGAN 模型下载"" [link](https://drive.google.com/drive/u/0/folders/17VYV_SoZZesU6mbxz2dMAIccSSlqLecY)")
    #     st.header("将图像放大为高清")
    #     st.text("上传图片")

    #     model_path = './RRDB_ESRGAN_x4.pth'  # models/RRDB_ESRGAN_x4.pth OR models/RRDB_PSNR_x4.pth
    #     # device = torch.device('cuda')  # if you want to run on CPU, change 'cuda' -> cpu
    #     device = torch.device('cpu')

    #     # test_img_folder = 'LR/*'
    #     uploaded_file = st.file_uploader("选择..", type=["jpg","png","jpeg"])
    #     if uploaded_file is not None:
    #         img = Image.open(uploaded_file).convert('RGB')
    #         st.image(img, caption='上传了图片。', use_column_width=True)
    #         st.write("")
    #         st.write("")
    #         st.write("放大图像，大约等待时间：1 分钟,请稍候...")

    #         rrdb_esrgan_model = arch.RRDBNet(3, 3, 64, 23, gc=32)
    #         rrdb_esrgan_model.load_state_dict(torch.load(model_path), strict=True)
    #         rrdb_esrgan_model.eval()
    #         rrdb_esrgan_model = rrdb_esrgan_model.to(device)

    #         idx = 0

    #         # img = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3) * 1.0 / 255
    #         # uploaded_file = st.file_uploader("Upload Image")
    #         # image = Image.open(uploaded_file)
    #         # st.image(image, caption='Input', use_column_width=True)
    #         img = np.array(img)* 1.0 / 255
    #         # cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

    #         img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    #         img_LR = img.unsqueeze(0)
    #         img_LR = img_LR.to(device)

    #         with torch.no_grad():
    #             output = rrdb_esrgan_model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    #         output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    #         output = torch.tensor((output * 255.0).round())
    #         fig1 = plt.figure(figsize=(14,8))

    #         fig1.suptitle("Upscaled image")
    #         plt.imshow(np.transpose(vutils.make_grid(output, padding=2, normalize=True), (0,1, 2)))  

    #         st.pyplot(fig1)

    # elif page =="生成动漫人脸图像":


    #         # Number of GPUs available. Use 0 for CPU mode.
    #         ngpu = 1

    #         # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    #         device = torch.device("cpu")
    #         # anime_face_gan_gen_model = AnimeFaceGenerator(ngpu).to(device)
    #         anime_face_gan_gen_model  = torch.load("./anime_face_gan_generator64_64.pt",map_location=torch.device('cpu') )
    #         pp1=st.slider("p1",-5.01,5.00)
    #         pp2=st.slider("p2",-5.01,5.00)
    #         pp3=st.slider("p3",-5.01,5.00)
    #         pp4=st.slider("p4",-5.01,5.00)
    #         pp5=st.slider("p5",-5.01,5.00)
    #         pp6=st.slider("p6",-5.01,5.00)
    #         pp7=st.slider("p7",-5.01,5.00)
    #         pp8=st.slider("p8",-5.01,5.00)
    #         anime_face_gan_gen_model.eval()
    #         bla = [pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8]
    #         randomlist = []
    #         for i in range(0,92):
    #             n = random.random()
    #             randomlist.append(n)
    #         res = bla + randomlist
    #         # print(res)

    #         fixed_noise = torch.tensor(res).reshape(1,100,1,1)



    #         # fixed_noise = torch.randn(1, nz, 1, 1, device=device)
    #         print(fixed_noise)
    #         fake = anime_face_gan_gen_model(fixed_noise)

    #         fig1 = plt.figure(figsize=(14,8))

    #         fig1.suptitle("随机生成的动漫脸")

    #         plt.imshow(np.transpose(vutils.make_grid(fake, padding=2, normalize=True), (1, 2, 0)))  

    #         st.pyplot(fig1)



elif authentication_status == False:
    st.error("用户名/密码不正确")
elif authentication_status == None:
    st.warning('请输入您的用户名和密码')








