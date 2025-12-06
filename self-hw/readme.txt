# HW3-資料庫設計 (現場作業)

## 檔案

1. aaaa.mermaid
2. Dockerfile
3. image.png 作業截圖
4. main.py 資料庫程式
5. mall.db
6. readme.txt
7. requirement.txt python 的依賴


### 使用 docker 執行

1. 安裝 docker:
https://www.docker.com/products/docker-desktop/

2. 打開 docker desktop
3. 將終端機路徑設定到 /411211480/ 下
4. (打包程式)在終端機中輸入: 
docker build -t my-db-app .

5. (執行程式)在終端機中輸入: 
Windows:
docker run -it --rm -v ${PWD}:/data my-db-app
Mac/ Linux:
docker run -it --rm -v "$(pwd)":/data my-db-app

6. 輸入姓名性別後，程式會將資料寫入資料庫，並讀取出來以供驗證

### 不使用 docker 執行程式

1. 安裝套件
pip install sqlalchemy

2. 執行程式：
python main.py

3. 輸入姓名性別後，程式會將資料寫入資料庫，並讀取出來以供驗證
