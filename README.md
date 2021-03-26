# **xcovid**

In this project we created a transfer learning based COVID-19 lung x-ray classifier WebApp for the [Scitek - POATEK Datathon](https://poatek.com/scitek/)!

In order to run it, just follow these instructions:
1. Clone the repository with `git clone https://github.com/gfc-fiscomp/xcovid.git`.
2. Get into the repository directory with `cd xcovid`.
3. Type `streamlit run app.py` on the terminal. A localhost instance should then open up in your browser! (note: the website is entirely in Brazilian Portuguese)

The model used for image classification is a ResNet50 pre-trained with ImageNet weights that was finetuned using the images providade in [this](https://drive.google.com/drive/folders/1Zk54BzZLyl6X_KTnksSysfHVSCDsx-un) dataset (given to us by the datathon organizers). In order to learn more about how the model was trained, check out the `rede.ipynb` file over [here](https://github.com/gfc-fiscomp/xcovid/blob/main/rede.ipynb). We had to deal with a very imbalanced dataset! The communication between the WebApp and the model is made possible by `call_model.py`, which can be seen over [here](https://github.com/gfc-fiscomp/xcovid/blob/main/call_model.py).

Here is the classifier's confusion matrix on test data:
![image](https://user-images.githubusercontent.com/47951223/112685128-e1b30380-8e52-11eb-898c-2bda2c3948a2.png)

If you'd like to test the WebApp for yourself we have two example images available in the `example_images` folder.

## Some images from the WebApp:

Home page:
![image](https://user-images.githubusercontent.com/47951223/112684311-9ba97000-8e51-11eb-9d8a-0e9d37d173c1.png)

Test page:
![image](https://user-images.githubusercontent.com/47951223/112684347-ae23a980-8e51-11eb-8d77-97edeb4d5b81.png)

A classified image:
![image](https://user-images.githubusercontent.com/47951223/112684407-c4316a00-8e51-11eb-94b3-a148067b807c.png)

About page:
![image](https://user-images.githubusercontent.com/47951223/112684432-cd223b80-8e51-11eb-87b9-b8feb6c5e1a5.png)
