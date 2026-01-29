🧠 AI Hedge Rotation System
Gold → Bitcoin Automatic Disaster Backup (Streamlit + Python)
🇸🇦 الشرح بالعربي

هذا المشروع عبارة عن نظام ذكاء اصطناعي لاكتشاف انهيار الذهب وتحويل المساعد التداولي تلقائيًا من تحليل الذهب إلى تحليل البيتكوين كخطة إنقاذ (Disaster Hedge).

الفكرة مبنية على مبدأ تستخدمه صناديق التحوط:

لا تتداول الأصل… بل تداول حالة السوق (Market Regime)

🎯 ماذا يفعل النظام؟

يقوم النظام بمراقبة حركة الذهب كل 15 دقيقة، وعند اكتشاف:

كسر متوسطات مهمة (EMA20 / EMA50)

هبوط قوي بزخم مرتفع

بداية موجة هبوط حادة

يقوم تلقائيًا بـ:

✅ إيقاف إشارات الذهب
✅ تفعيل إشارات البيتكوين
✅ اعتبار السوق في وضع "Risk / Crash Mode"

وعند تعافي الذهب، يعود النظام تلقائيًا للعمل على الذهب.

🧠 مكونات النظام

المشروع يتكون من 4 ملفات رئيسية:

الملف	الوظيفة
regime_detector.py	العقل الرئيسي — يحدد هل السوق Gold أو Bitcoin
gold_analyzer.py	استخراج إشارات الذهب
btc_analyzer.py	استخراج إشارات البيتكوين
app.py	واجهة Streamlit وتشغيل النظام
⚙️ آلية العمل
إذا كان الذهب في اتجاه هابط قوي
    → الوضع يتحول إلى BITCOIN
غير ذلك
    → يبقى على GOLD


هذا يسمى:

Market Regime Detection AI

🛡️ لماذا هذا مهم؟

في حالات انهيار الذهب (أخبار الفيدرالي – ارتفاع الدولار – ارتفاع العوائد):

الذهب ينهار بسرعة

البيتكوين يتحرك بشكل مختلف أو يصبح أداة تحوط

النظام يستفيد من هذه العلاقة بشكل تلقائي.

🚀 طريقة التشغيل
pip install -r requirements.txt
streamlit run app.py

📦 المتطلبات

Python 3.10+

Streamlit

yfinance

pandas

💡 الفكرة المتقدمة

هذا المشروع لا يتداول أصلًا ماليًا…
بل يتداول حالة السوق مثل الأنظمة الاحترافية في صناديق التحوط.

🇬🇧 English Description

This project is an AI Market Regime Detection System that automatically switches your trading assistant from Gold analysis to Bitcoin analysis when a gold crash is detected.

The concept is inspired by hedge funds:

Don’t trade the asset… trade the market regime.

🎯 What does the system do?

The system monitors gold price action every 15 minutes. When it detects:

EMA20 breaking below EMA50

Strong downside momentum

Early signs of a gold crash

It automatically:

✅ Disables Gold signals
✅ Activates Bitcoin signals
✅ Switches to "Risk / Crash Mode"

When gold recovers, the system automatically switches back to gold.

🧠 System Components

The project consists of 4 main files:

File	Role
regime_detector.py	The brain — decides GOLD or BITCOIN mode
gold_analyzer.py	Generates gold signals
btc_analyzer.py	Generates bitcoin signals
app.py	Streamlit UI and system runner
⚙️ Logic
IF gold is in strong downtrend
    → Switch to BITCOIN mode
ELSE
    → Stay in GOLD mode


This is called:

Market Regime Detection AI

🛡️ Why this is powerful?

During events like:

Federal Reserve news

DXY spike

Yield spike

Risk-off panic

Gold can crash rapidly, while Bitcoin behaves differently.

The system exploits this relationship automatically.

🚀 How to run
pip install -r requirements.txt
streamlit run app.py

📦 Requirements

Python 3.10+

Streamlit

yfinance

pandas

💡 Advanced Concept

This project does not trade an asset…

It trades the market condition, similar to professional hedge fund systems
