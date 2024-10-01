**一、摘要**

近年來國人得到糖尿病的比例持續增加，位居十大死因中的第五名。糖尿病屬於慢性疾病，與家族遺傳、環境因素息息相關。本次實驗，我們將設計程式以找出以下因素與糖尿病的相關程度：１懷孕次數、２血液中葡萄糖濃度、３舒張壓、４三頭肌皮摺厚度、５胰島素濃度、６ BMI值、７糖尿病函數。使用ｋｎｎ、隨機森林、決策樹等機器學習方法去比對最終果和找出各個因素與糖尿病的相關程度，也可以此比較各個演算法的準確度。

**二、簡介**

機器學習演算法是一種讓電腦自動學習的方法。透過大量數據找出規律，並利用此規律對測試資料進行預測。其中，機器學習演算法又可分為以下四類：監督式學習、非監督式學習、半監督式學習、強化學習。

為找出與糖尿病最相關的因素，本實驗建置三個機器學習演算法，分別是、決策樹，與隨機森林，將懷孕次數、血液中葡萄糖濃度、舒張壓、三頭肌皮摺厚度、胰島素濃度、值、糖尿病函數輸入至本系統，以利機器學習，找出各個因素與糖尿病的相關程度，也可以此比較各個演算法的準確度。


**三、結果分析**

*隨機森林的正確率略高於決策樹，決策樹加上Bagging後會增加其正確率。
![image](https://github.com/user-attachments/assets/3cfda7b0-97f9-4888-8d83-6f3327760aa3)

*決策樹 V.S 隨機森林
![image](https://github.com/user-attachments/assets/68ed0025-fa2e-48ff-bad7-a6381866c83e)

*四種方式測試七項因素與糖尿病相關性
1. Decision tree
   
   ![image](https://github.com/user-attachments/assets/925108db-56af-4153-8556-cefc474d7901)

2. Decision tree (best depth)
   
   ![image](https://github.com/user-attachments/assets/078c54f3-6a31-4e3b-b3a7-5d1f7c18066f)

3. Decision tree (Bagging)

   ![image](https://github.com/user-attachments/assets/e26513ca-c8e1-4098-a245-401f744b5707)

4. Random forest

   ![image](https://github.com/user-attachments/assets/c17f82ec-c3db-4b81-87fc-ad689a39206a)


**-------------------------------------------------------------------------------------------------------------------------------------------------------**

詳情請看[書面報告](https://github.com/ChingJuYeh/DataMining/blob/main/%E6%9B%B8%E9%9D%A2%E5%A0%B1%E5%91%8A.docx) 
