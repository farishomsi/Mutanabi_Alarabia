## Mutanabi_Alarabia
اول منصة مخصصة للطلبة و الباحثين، تقوم بتحليل  كامل للكلمة، من كل الجوانب التي قد يحتاجها الطالب، و تقوم بتوفير هذا التحليل بضغطة زر، و بلمح البصر.


![](متنبئ.png)


بعد دراسة الحلول الموجودة، و المشاكل التي تواجه مستخدميها، توصلنا إلى حلنا الإبداعي، حلنا الإبداعي هو متنبئ العربية، و هو أول منصة مخصصة للطلبة و الباحثين، تقوم بتحليل  كامل للكلمة، من كل الجوانب التي قد يحتاجها الطالب، و تقوم بتوفير هذا التحليل بضغطة زر، و بلمح البصر.‎
 و هو أول منصة مخصصة للطلبة و الباحثين، تقوم بتحليل  كامل للكلمة، من كل الجوانب التي قد يحتاجها الطالب، و تقوم بتوفير هذا التحليل بضغطة زر، و بلمح البص
  
  ## النموذج 
 
  

.
وظفنا النموذج (و الذي يعتبر بهيكلية  system of models) ليقوم ب ٦ عمليات رئيسية في معالجة اللغة العربية:
### الاول : تلخيص(summarization)

يقوم بتلخيص الفقرات تلخيص فعال  مع المحافظة على المعنى الأصلي و احتواءه على جميع الأفكار الأساسية من الفقرات الرئيسية بحيث استخدمنا (TF-IDF) لحساب ال frequency للكلمات و تطبيع خوارزمية Text Ranking.

### الثاني: تشكيل

بحيث طورنا موديل يساعد على التشكيل آخذاً بعين الاعتبار موقع الكلمات بالجمل (اعرابها).


### الثالث : التصحيح التلقائي  (autocorrector) 

سيقوم النموذج بإيجاد الكلمات المكررة ووضع تكرارات معين لكل كلمة ثم يقوم بحساب احتمالية ظهور كل كلمة 
اذا كانت هنالك كلمات بحاجة للتعديل فيقوم هذا البرنامج بتنظيف الكلمات وحذف الحروف الزائدة وتبديل أية حروف خاطئة بمرادفها الصحيح وفي آخر خطوة يتم تبديل  الكلمة الصحيحة بدلاً من الكلمة التي كانت تحوي أخطاء


### الرابع : مستخرج
نموذج يساعد على استخراج الاصل المعجمي و الجذر ، اقسام الكلام جمع التكسير ان وجد.


### الخامس : متنبئ

بحيث يقترح و يتوقع الكلام في مكان محدد من الجملة 

### السادس : مصنف اللهجات 
يقوم بتصنيف اللهجات العربية و تحديدها ل ٢٥ لهجة منها ( الاردنية ، السعودية ، المصرية ، المغربية)


وتم تطبيق نموذج الذكاء الاصطناعي على chrome extension ليتم استخدامه من قبل مختلف المستخدمين بسهولة تامة عند الحاجة

لرؤية التطبيق شاهد الفيديو  عبر الرابط التالي :

https://drive.google.com/file/d/14frXMRIprI6tzjnQxnbIhE-vqKltVuhv/view?usp=sharing 



لرؤية مثال اختبار النماذج عبر الرابط التالي:

https://drive.google.com/file/d/1nlbFKCzSqSz9n7FGSPmAG9Iyn0QonR43/view?usp=sharing
