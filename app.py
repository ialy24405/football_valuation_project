import streamlit as st
import pandas as pd
import joblib

# 1. إعدادات الصفحة
st.set_page_config(page_title="الكشاف الآلي | Football Scout", page_icon="⚽", layout="centered")

# 2. تحميل الموديل
# (تأكد إن مسار واسم الموديل مطابق للي إنت حفظته)
@st.cache_resource
def load_model():
    return joblib.load('models/RandomForestModel.pkl')

try:
    model = load_model()
except FileNotFoundError:
    st.error("❌ لم يتم العثور على ملف الموديل! تأكد من حفظه في مجلد models باسم rf_model.pkl")
    st.stop()

# 3. واجهة المستخدم (UI)
st.title("⚽ الكشاف الآلي | تقييم أسعار اللاعبين")
st.markdown("أدخل مواصفات اللاعب هنا وسيقوم الذكاء الاصطناعي بتوقع سعره العادل في السوق.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.slider("العمر", min_value=15, max_value=45, value=20)
    position = st.selectbox("المركز", ['CAM', 'CB', 'CDM', 'CF', 'CM', 'GK', 'LB', 'LM', 'LW', 'LWB', 'RB', 'RM', 'RW', 'RWB', 'ST'])

with col2:
    overall = st.slider("التقييم الحالي (Overall)", min_value=40, max_value=99, value=75)
    potential = st.slider("التقييم المتوقع (Potential)", min_value=40, max_value=99, value=80)

# 4. التوقع عند الضغط على الزر
st.divider()
if st.button("💰 احسب السعر العادل", use_container_width=True):
    # تجهيز البيانات
    input_data = {
        'age': [age],
        'overall': [overall],
        'potential': [potential],
        position: [1] # المركز اللي اختاره هياخد 1
    }
    
    df_input = pd.DataFrame(input_data)
    
    # سحب أسماء العواميد اللي الموديل اتدرب عليها عشان نظبط الأصفار
    model_cols = model.feature_names_in_
    df_input = df_input.reindex(columns=model_cols, fill_value=0)
    
    # التوقع
    prediction = model.predict(df_input)[0]
    
    # عرض النتيجة بشياكة
    st.success(f"### السعر العادل المتوقع: {prediction:,.0f} يورو")
    # if prediction > 50000000:
        # st.balloons() # احتفال لو اللاعب طلع غالي!