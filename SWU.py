import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from PIL import Image

img_hortyca_1 = Image.open("images/H1.jpg")
img_hortyca_2 = Image.open("images/H2.jpg")
img_hortyca_3 = Image.open("images/H3.jpg")

img_hersones_1 = Image.open("images/HT1.jpg")
img_hersones_2 = Image.open("images/HT2.jpg")
img_hersones_3 = Image.open("images/HT3.jpg")

img_kamyanets_1 = Image.open("images/K1.jpg")
img_kamyanets_2 = Image.open("images/K2.jpg")
img_kamyanets_3 = Image.open("images/K3.jpg")

st.set_page_config(page_title="Сім чудес України", page_icon=":european_post_office:", layout="wide")

st.header("Сім чудес України :blue_heart::yellow_heart:" )
selected = option_menu(
menu_title = None,
options = ["Хортиця","Херсонес","Кам'янець-Подільський"],
default_index=0,
orientation= "horizontal",
)

if selected == "Хортиця":
    with st.container():
        st.write("---")
        st.subheader("""Хортиця - унікальний острів на Дніпрі""")
        picture_column, text_column = st.columns(2)

        with picture_column:
            st.image(img_hortyca_1)
        with text_column:
            st.write("""Острів Хортиця – найбільший острів на Дніпрі, унікальність якого – у рідкісному поєднанні на одній території різноманітних природних комплексів, пам’яток геології, культури, історії.""")
            st.write("""Основу найбільшого острова на Дніпрі (довжина 12, ширина, в середньому, 2,5 км, загальна площа – 2360 га) складають граніти і гнейси, яким близько двох мільярдів років. Природна унікальність Хортиці в тому, що тут у мініатюрі представлені зразки всіх ландшафтних зон України.""")
            st.write("""Дуже важливою та значущою є історична спадщина цього краю. Саме тут, за однією з версій, навесні 972 р. загинув Київський князь Святослав Ігоревич – одна з найяскравіших постатей давньої історії України. Вважається, що з Хортиці вирушали у козацькі походи проти поляків оспівані українським народом Северин Наливайко, Криштов Косинський, Іван Сулима. Бував тут і гетьман Петро Сагайдачний зі своїм військом. Саме на Хортиці Богдан Хмельницький отримав підтримку реєстрових козаків у часи Визвольної війни у 1648–1654 рр.""")    
            st.write("""Розкопки, проведені археологами заповідника, дають підстави стверджувати, що один із прототипів Запорозької Січі, її предтеча, існувала на Хортиці біля плавневої частини. Саме тут виявлено військове поселення Х–ХІV ст.""")
    st.write("Сьогодні завершилося будівництво історико-культурного комплексу “Запорозька Січ”, яке розпочалося у 2004 р. на свято Покрови, у День українського козацтва.")
    st.write("У Музеї історії запорозького козацтва, відкритому на території заповідника у 1983 р., зібрано понад 30 тис. експонатів, які охоплюють історичний період від палеоліту до ХІХ ст. н. е. Експозицію доповнюють чотири діорами. Переважна більшість експонатів знайдена саме на Хортиці. Це – кам’яні знаряддя праці, кераміка, зброя, якорі, фрагменти старовинних човнів, стовбур дуба, який був зрубаний кілька тисячоліть тому і стільки ж пролежав на Дніпровському дні.")

    with st.container():
        picture_column_1, picture_column_2 = st.columns(2)

        with picture_column_1:
            st.image(img_hortyca_2)
        with picture_column_2:
            st.image(img_hortyca_3)
        with st.expander("Додаткова інформація"):
                with st.container():
                    video_column, map_column = st.columns(2)

                    with video_column:
                        st.write("Відеоекскурсія по острову Хортиця")
                        st.video(data="https://www.youtube.com/watch?v=jqSkfShpwU4")
                    with map_column:

                        st.write("Місце знаходження острова та  історико-культурного комплексу “Запорозька Січ”")
                        l = folium.Map(location=[47.85753, 35.07555], zoom_start=13)
                        folium.Marker(
                            [47.85753, 35.07555],
                            popup="Хортиця",
                            tooltip="Хортиця"
                        ).add_to(l)
                        st_data = st_folium(l, width=670, height=490)
if selected == "Херсонес":
    with st.container():
        st.write("---")
        st.subheader("Херсонес Таврійський - місто давніх греків!")
        text_column, picture_column = st.columns(2)

        with text_column:
            st.write("Херсонес Таврійський – таку назву носило місто, засноване давньогрецькими колоністами понад дві з половиною тисячі років тому на південному заході Кримського півострова.")
            st.write("Слово „Херсонес” зазвичай перекладають з грецької як „півострів”. Місто дійсно було розташоване на невеличкому півострові поміж двох бухт. Таври – войовниче плем’я, що заселяло сусідні гористі місцевості, – спричинили народження епітету „Таврійський”.")
            st.write("Територія Херсонеса досліджується археологами уже 180 років. За цей час відкрито понад третину міста. Серед археологічних знахідок є унікальні – присяга громадян Херсонеса ІІІ ст. до н.е., декрети, фрески, мозаїки, шиферні ікони християнських храмів, написи-присвяти, численні побутові предмети. Загалом музейні зібрання заповідника нараховують понад 200 тисяч експонатів.")    
            st.write("Сьогодні Ви зможете провести у заповіднику цілий день, розглядаючи численні експонати або просто насолоджуючись прогулянкою по території стародавнього городища. Можна здійснити й віртуальну екскурсію, скориставшись картою, на якій позначені розкопані ділянки міської території. А ті, хто особисто бажає взяти участь у розкопках, можуть зробити це, попередньо домовившись з адміністрацією.")

        with picture_column:
            st.image(img_hersones_2)

    # st.write("Сьогодні Ви зможете провести у заповіднику цілий день, розглядаючи численні експонати або просто насолоджуючись прогулянкою по території стародавнього городища. Можна здійснити й віртуальну екскурсію, скориставшись картою, на якій позначені розкопані ділянки міської території. А ті, хто особисто бажає взяти участь у розкопках, можуть зробити це, попередньо домовившись з адміністрацією.")

    with st.container():
        picture_column_1, picture_column_2 = st.columns(2)

        with picture_column_1:
            st.image(img_hersones_3)
        with picture_column_2:
            st.image(img_hersones_1)
        with st.expander("Додаткова інформація"):
                with st.container():
                    map_column,video_column  = st.columns(2)
                    with map_column:

                        st.write("Місце знаходження Херсонесу")
                        l = folium.Map(location=[44.6117611, 33.4889364], zoom_start=13)
                        folium.Marker(
                            [44.6117611, 33.4889364], 
                            popup="Херсонес",
                            tooltip="Херсонес"
                        ).add_to(l)
                        st_data = st_folium(l, width=670, height=490)
                    with video_column:
                        st.write("Відеоекскурсія Херсонесом")
                        st.video(data="https://www.youtube.com/watch?v=rsY20S1Ttb8")

if selected == "Кам'янець-Подільський":
    with st.container():
        st.write("---")
        st.subheader("""Кам’янець-Подільський – місто, що зберегло дух середньовіччя.""")
        picture_column, text_column = st.columns(2)

        with picture_column:
            st.image(img_kamyanets_1)
        with text_column:
            st.write("Своєрідність і унікальність його полягають у гармонійному поєднанні ландшафту з містобудівною структурою середньовічного міста, в якому військові інженери, використовуючи чудові природні властивості, створили фортифікаційну систему, що не має аналогів у Європі.")
            st.write("Кам’янець-Подільський хоч не є обласним центром, проте займає третє місце після Києва та Львова за кількістю пам’яток старовини і культури.")
            st.write("Національний історико-архітектурний заповідник „Кам’янець” є одним із найстаріших на території України. Загальна площа заповідника сягає 121 га та налічує майже 200 пам’яток архітектури.")    
            st.write("Сьогодні чимало туристів висловлюють захоплення вдалим поєднанням потужних оборонних мурів міста, Старого замку (XII–XVIII ст.) та високих стрімких скель каньйону річки Смотрич.")
            st.write("Неабиякий інтерес викликає і унікальний Замковий міст, що сполучає Старе місто із Замковим комплексом. Досі існує немало суперечок щодо його походження. ")
            st.write("До складу Кам’янецької фортеці входять одинадцять башт, кожна з яких має свою назву й історію. ")

    with st.container():
        picture_column_1, picture_column_2 = st.columns(2)

        with picture_column_1:
            st.image(img_kamyanets_2)
        with picture_column_2:
            st.image(img_kamyanets_3)
        with st.expander("Додаткова інформація"):
                with st.container():
                    video_column, map_column = st.columns(2)

                    with video_column:
                        st.write("Відеоекскурсія замком")
                        st.video(data="https://www.youtube.com/watch?v=dTnRNN46SUE")
                    with map_column:

                        st.write("Кам'янець-Подільський на карті")
                        l = folium.Map(location=[48.6734848, 26.5610911], zoom_start=13)
                        folium.Marker(
                            [48.6734848, 26.56109115],
                            popup="Кам'янець-Подільський",
                            tooltip="Кам'янець-Подільський"
                        ).add_to(l)
                        st_data = st_folium(l, width=670, height=490)



        

