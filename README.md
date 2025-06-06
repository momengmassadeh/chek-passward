برنامج بسيط مكتوب بلغة Python يقوم بتحليل كلمة المرور المدخلة من قبل المستخدم وتقييم مدى قوتها بناءً على معايير أمان شائعة. يهدف البرنامج إلى مساعدة المستخدمين على اختيار كلمات مرور قوية تحمي حساباتهم من الاختراق.

🛠️ التقنيات المستخدمة:
اللغة: Python 3

المكتبة:

re (Regular Expressions) للتحقق من وجود أنماط معينة في كلمة المرور مثل الأحرف، الأرقام، والرموز.

⚙️ آلية العمل:
يطلب البرنامج من المستخدم إدخال كلمة المرور.

يقوم بفحص العناصر التالية:

الطول (8 أحرف على الأقل).

وجود حرف صغير (a-z).

وجود حرف كبير (A-Z).

وجود رقم (0-9).

وجود رمز خاص (!@#$%^&* وغيرها).

يعرض ملاحظات حول العناصر المفقودة إن وُجدت.

يعرض النتيجة: "كلمة المرور قوية ✅" أو "كلمة المرور ضعيفة ❌" مع شرح السبب.

🎯 أهداف المشروع:
تعليم المستخدمين مبادئ أمان كلمات المرور.

تدريب على استخدام التعبيرات النمطية (regex).

تقديم أداة مفيدة ضمن تطبيقات تسجيل الدخول أو التحقق الأمني.

💡 ملاحظة:
هذا البرنامج لا يحفظ كلمات المرور ولا يرسلها لأي جهة. هو أداة تعليمية وتوعوية فقط.

هل ترغب أن أكتب هذا الوصف على شكل ملف README.md لك؟
