# CDMS_2023_Project1 ：bookstore项目报告

| 课程名称：当代数据管理系统 | 项目名称：bookstore | 指导老师：周烜 |
| -------------------------- | ------------------- | -------------- |
| 成员：李嘉豪               | 学号：10204804434   | 年级：2021     |
| 成员：杨茜雅               | 学号：10215501435   | 年级：2021     |
| 成员：王溢阳               | 学号：10204602470   | 年级：2021     |

## 一. 实验要求

- 实现一个提供网上购书功能的网站后端
  - 网站支持书商在上面开商店，购买者可以通过网站购买。买家和卖家都可以注册自己的账号。一个卖家可以开一个或多个网上商店，买家可以为自已的账户充值，在任意商店购买图书。
  - 支持 下单->付款->发货->收货 流程

- 功能

  - 1.实现对应接口的功能，见项目的doc文件夹下面的.md文件描述 （60%），其中包括：

    - 1)用户权限接口，如注册、登录、登出、注销

    - 2)买家用户接口，如充值、下单、付款

    - 3)卖家用户接口，如创建店铺、填加书籍信息及描述、增加库存

      **通过对应的功能测试，所有test case都pass**

  - 2.为项目添加其它功能 ：（40%）
    - 1)实现后续的流程：发货 -> 收货
    - 2)搜索图书
      - 用户可以通过关键字搜索，参数化的搜索方式；
      - 如搜索范围包括，题目，标签，目录，内容；全站搜索或是当前店铺搜索。
      - 如果显示结果较大，需要分页 (使用全文索引优化查找)

  - 3)订单状态，订单查询和取消定单
    - 用户可以查自已的历史订单，用户也可以取消订单。取消定单可由买家主动地取消定单，或者买家下单后，经过一段时间超时仍未付款，定单也会自动取消。

- 要求

  - 2～3人一组，做好分工，完成下述内容：

    - bookstore文件夹是该项目的demo，采用flask后端框架与sqlite数据库，实现了前60%功能以及对应的测试用例代码。

      - **要求大家创建本地 MongoDB 数据库，将`bookstore/fe/data/book.db`中的内容以合适的形式存入本地数据库，后续所有数据读写都在本地的 MongoDB 数据库中进行**
      - 书本的内容可自行构造一批，也可参从网盘下载，下载地址为：https://pan.baidu.com/s/1bjCOW8Z5N_ClcqU54Pdt8g

        提取码：hj6q

    - 在完成前60%功能的基础上，继续实现后40%功能，要有接口、后端逻辑实现、数据库操作、代码测试。对所有接口都要写test case，通过测试并计算测试覆盖率（尽量提高测试覆盖率）。

    - 尽量使用索引，对程序与数据库执行的性能有考量

    - 尽量使用git等版本管理工具

    - 不需要实现界面，只需通过代码测试体现功能与正确性

- 报告内容

  - 每位组员的学号、姓名，以及分工

  - 文档数据库设计：文档schema

  - 对60%基础功能和40%附加功能的接口、后端逻辑、数据库操作、测试用例进行介绍，展示测试结果与测试覆盖率。

  - 如果完成，可以展示本次大作业的亮点，比如要求中的“3 4”两点。

    注：验收依据为报告，本次大作业所作的工作要完整展示在报告中

- 考核标准

  1. 没有提交或没有实质的工作，得D
  
  2. 完成"要求"中的第1点，可得C
  
  3. 完成前3点，通过全部测试用例且有较高的测试覆盖率，可得B
  
  4. 完成前2点的基础上，体现出第3 4点，可得A
  
  5. 以上均为参考，最后等级会根据最终的工作质量有所调整
  

## 二. 项目运行

- **目录结构**

  ```
  bookstore
    |-- be                            后端
          |-- model                     后端逻辑代码
          	|-- operations.py         	后40%功能代码
          	|-- ....                     
          |-- view                      访问后端接口
          |-- ....
    |-- doc                           JSON API规范说明
    |-- fe                            前端访问与测试代码
          |-- access
          |-- bench                   效率测试
          |-- data
              |-- book.db             sqlite 数据库(book.db，较少量的测试数据)
              |-- scraper.py          从豆瓣爬取的图书信息数据的代码
          |-- test                    功能性测试（包含对前60%功能的测试）
          |-- conf.py                 测试参数，修改这个文件以适应自己的需要
          |-- conftest.py             pytest初始化配置，修改这个文件以适应自己的需要
          |-- ....
    |-- be_rewrite.py                 改写be.db
    |-- book_rewrite.py               改写book.db
    |-- ER图
    |-- 2023_ECNU_PJ1_report.pdf      项目报告
    |-- ....
  ```

- **安装配置**

  - requirements

    ```python
    simplejson==3.19.2
    lxml==4.9.2
    codecov==2.1.13
    coverage==7.3.2
    flask==2.0.0
    pre - commit==1.3.0
    pytest==7.4.0
    PyJWT==2.4.0
    requests==2.31.0
    Werkzeug>=2.0==2.0.0
    Jinja2>=3.0==3.1.2
    itsdangerous>=2.0==2.1.2
    click>=7.1.2==8.1.7
    iniconfig==1.1.1
    packaging==23.0
    pluggy<2.0,>=0.12==1.0.0
    idna<4,>=2.5==3.4
    urllib3<3,>=1.21.1==1.26.16
    certifi>=2017.4.17==2023.7.22
    MarkupSafe>=2.0==2.1.1
    ```

  - **python 3.12**

  - **项目运行**

    - 进入bookstore文件夹下：

    - 安装依赖
  
    
    ```
    pip install -r requirements.txt
    ```
    
    - 初始化数据库
    
    
    ```python
    python book_rewrite.py
    python be_rewrite.py
    ```
  
    - 运行后端服务器
    
    
    ```python
    python3 app.py
    ```
    
    - 执行测试
    
    
    ```
    bash script/test.sh
    ```
  
  



## 三. 文档数据库设计

### 3.1 设计思路及数据库转化

一共两个SQLite数据库：be.db和book.db

**be.db**

- user：记录用户id
- user_store：其对应的店铺id

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps1.jpg" alt="img" style="zoom:60%;" /> 

**book.db**：书的基本信息

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps2.jpg" alt="img" style="zoom:60%;" /> 

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps3.jpg" alt="img" style="zoom:60%;" /> 

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps4.jpg" alt="img" style="zoom:60%;" /> 

>  数据库设计
>
> ​	book、store、user、new_order_detail、new_order和user_store【共计5张表，表格结构见下文“3.3 表格结构”】

**关系描述**

- store 和 book：一对多，表示一个商店可以销售多本书。通过 store 实体中 book_id 实现关联。
- user 和 new_order：一对多，表示一个用户可以有多个订单。通过 new_order实体中 order_id 实现关联。
- new_order 和 new_order_detail：一一对应，通过 order_id 字段实现关联。
- user 和 store：一对多，表示一个用户（卖家）可以开多个商店。通过 user_store 实体建立关联。
- store 和 new_order：一对多，表示一个商店可以有多个订单。通过store 实体中 store_id 实现关联。
- user 和 user_store：一一对应，通过 两个实体中 user_id 实现关联。



#### 3.1.1 **设计思路**

- **书籍详细信息：**独立存储在 book 表中，避免冗余、便于管理。
- **商店和库存管理：**store 连接书籍和商店，便于跟踪每本书在不同商店的库存和价格，为库存管理提供基础。
- **用户信息安全：**user 中的密码字段应使用加密存储，token 字段用于认证和会话管理，提高安全性。
- **订单处理：**new_order 和 new_order_detail 之间的关系允许系统记录订单的总体信息和具体的每项订单细节，如单个书籍的购买数量和价格等。有助于简化订单处理流程和历史订单的查询。
- **用户商店关系：**user_store 说明一个用户可以有多个商店，为平台上的卖家提供了灵活性。
- **数据正规化：**通过关联不同的表，避免数据冗余，使数据库正规化。例如，书籍信息、用户信息、订单信息都分别存储在独立的表中，表与表之间可以有关联。
- **扩展性和灵活性**：考虑到了未来可能的扩展性，如添加新的字段或表以支持新功能【亮点功能：推荐系统】
- **性能考量：**分开存储信息可以提高查询效率，特别是对复杂查询操作，如联合多个表来检索订单详情或计算商店的总销售额等。

​	总的来说，我们提供了一个结构化且灵活的数据库设计，它能够支持一个在线书店后端所需的所有基本功能，包括用户管理、库存管理、订单处理以及书籍的搜寻和购买。同时，它也考虑到了安全性、性能和未来的可扩展性。

#### 3.1.2 数据库转化

​	根据demo给出的be.db和book.db 两个SQLite 数据库，需要创建本地MongoDB 数据库，进行从 SQLite 数据库到 MongoDB 数据库的数据迁移操作。

**book.db数据库迁移**

​	**定义构造函数**：data_construct 函数接受一个包含书籍信息的行（line），将这些信息构造成一个字典（one_data），字典的键是书籍的各个属性，值是来自输入行的相应数据。

 <img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps5.jpg" alt="img" style="zoom:60%;" /> 

​	**连接 SQLite 数据库**：使用 sqlite3.connect 连接到名为 book.db 的 SQLite 数据库文件，并创建一个游标 cur_s 以便执行 SQL 查询。

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231106213017454.png" alt="image-20231106213017454" style="zoom:50%;" /> 

​	**连接 MongoDB 数据库**：使用 pymongo.MongoClient 连接到运行在本地的 MongoDB 实例，选择 bookstore 数据库，以及该数据库中的 book 集合（类似于 SQL 中的表）。

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps7.jpg" alt="img" style="zoom:50%;" /> 

​	**执行 SQL 查询**：构造一个 SQL 查询，选择 book 表中所有的列，并执行这个查询。

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps8.jpg" alt="img" style="zoom:50%;" /> 

​	**数据迁移**：对于 SQL 查询的结果，迭代每一行结果，使用 data_construct 函数将每行数据转换为字典，并将这些字典存储在 book_data 列表中。最后，使用 MongoDB 的 insert_many 方法将这个列表中的所有字典插入到 MongoDB 的 book 集合中。

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps9.jpg" alt="img" style="zoom:50%;" /> 

**be.db数据库迁移**

由于be.db数据库中只有user和user_store表是有数据的，只需要进行数据迁移操作。

​	**定义数据构造函数**

​		user_data_construct：这个函数负责将 user 表中的一行数据转换成字典格式。

​		user_store_data_construct：这个函数负责将 user_store 表中的一行数据转换成字典格式。

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps10.jpg" alt="img" style="zoom:50%;" /> 

这两个函数的目的是为了将 SQLite 数据库中的表行数据转换为 MongoDB 可以接受的文档（字典）格式。





**连接数据库**

​	通过 sqlite3.connect 连接到 SQLite 数据库文件（./fe/data/be.db）。

​	使用 pymongo.MongoClient 连接到本地运行的 MongoDB 实例，并选择 bookstore 数据库中的 user 和 user_store 集合。

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps11.jpg" alt="img" style="zoom:67%;" /> 

**迁移user表**

​	使用 SQL 语句从 SQLite 的 user 表中查询所需的字段。

​	通过迭代查询结果，使用 user_data_construct 函数构造字典列表。

​	使用 MongoDB 的 insert_many 方法批量插入字典列表到 user 集合中。

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps12.jpg" alt="img" style="zoom:67%;" /> 

**迁移user_store表**

​	使用 SQL 语句从 SQLite 的 user_store 表中查询所需的字段。

​	与 user 表类似，迭代查询结果，并使用 user_store_data_construct 函数构造字典列表。

​	使用 insert_many 方法批量插入字典列表到 user_store 集合中。

<img src="file:///C:\Users\86133\AppData\Local\Temp\ksohtml15296\wps13.jpg" alt="img" style="zoom:67%;" /> 



### 3.2 ER图

> 参考“3.1.1设计思路”
>
> 绘图软件：Visual Paradigm 17.1

![ER图](C:\Users\86133\Desktop\CDMS-2023\ER图.png)

**注：其中三分支箭头表示一对多的关系，单箭头表示一对一的关系**

### 3.3 表格结构

#### 3.3.1 book

| id     | title            | author | publisher | original_title   | translator | pub_year | pages | price | currency_unit | binding   | isbn   | author_intro | book_intro | content  | tags | picture  |
| ------ | ---------------- | ------ | --------- | ---------------- | ---------- | -------- | ----- | ----- | ------------- | --------- | ------ | ------------ | ---------- | -------- | ---- | -------- |
| 书本id | 书本名称（中文） | 作者   | 出版社    | 书本名称（原名） | 译者       | 出版年份 | 页数  | 价格  | 货币单位      | 精装/平装 | isbn码 | 作者简介     | 书本介绍   | 内容摘要 | 标签 | 书本图片 |

**注：书本id仅表示表里所有信息相同的书，不包含书名相同但是译者信息等不同的一类书。**

#### 3.3.2 user

| user_id | password | balance | tocken       | terminal       |
| ------- | -------- | ------- | ------------ | -------------- |
| 用户id  | 用户密码 | 余额    | 终端信息记录 | 登录时的终端号 |

**注：一个用户既可以买书又可以卖书，user_id仅代表bookstore中一个用户的账号**

#### 3.3.3 user_store

| user_id | store_id |
| ------- | -------- |
| 卖家id  | 店铺id   |

#### 3.3.4 new_order

| order_id | user_id | store_id | payment_time |
| -------- | ------- | -------- | ------------ |
| 订单id   | 买家id  | 店铺id   | 付款时间     |

#### 3.3.5 new_order_detail

| order_id | book_id | price | count | state                              | order_time | delivery_time | receipt_time | payment_time |
| -------- | ------- | ----- | ----- | ---------------------------------- | ---------- | ------------- | ------------ | ------------ |
| 订单id   | 书本id  | 价格  | 数目  | 状态（下单0、付款1、发货2、收货3） | 下单时间   | 发货时间      | 收货时间     | 付款时间     |

**注：新增column有state\order_time\delivery_time\receipt_time\payment_time。主要用于订单状态的记录。超时1小时未付款订单自动取消。**

#### 3.3.6 store

| store_id | book_id | price | stock_level |
| -------- | ------- | ----- | ----------- |
| 店铺id   | 书本id  | 价格  | 库存        |

**注：由于之前注释过的书本id仅表示所有信息相同的书，不包括名字相同其他信息稍有不同的一类书。此处的库存仅代表该书本的数量。**

## 四. 功能函数

### 前60%基本功能

#### 4.1 用户功能

​	交易平台当中用户部分的基本功能有：注册、注销、登录、登出、修改密码等。其中，对于用户信息来说不同需求对应不同的设计，本项目中的用户信息内容见“3.3.2 user”。其中功能代码见be/model/user.py

> 需求分析及后端逻辑
>
> - 注册
>   - 生成终端标识
>   - 生成JWT Token(包含用户ID、终端标识和当前时间戳)
>   - 检查用户是否已经存在，可返回错误代码并显示“该账号已被注册”
>   - 创建用户（包含用户ID、密码、余额、TWT Token和终端标识）
>   - 异常处理901、成功执行200

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230154592.png" alt="image-20231102230154592" style="zoom: 40%;" />

> - 检查Token（安全措施：确认用户正确登录并持有有效Token）
>   - 获取用户信息、检查用户是否存在
>   - 从数据库中获取Token并解码
>   - 验证Token是否匹配并检查有效期（3600秒）

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230242048.png" alt="image-20231102230242048" style="zoom:40%;" />

> - 检查user_id对应的密码是否正确
>   - 获取用户信息
>   - 获取密码并比较验证
> - 登录
>   - 校验密码
>   - 生成新Token
>   - 更新数据库记录

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230322680.png" alt="image-20231102230322680" style="zoom: 40%;" />

> - 登出
>   - 验证Token
>   - 生成新Token和终端标识
>   - 更新数据库记录

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230341110.png" alt="image-20231102230341110" style="zoom: 40%;" />

> - 注销账户 
>   - 删除用户记录

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230405830.png" alt="image-20231102230405830" style="zoom:40%;" />

> 更改密码
>
> - 验证旧密码
> - 生成新的Token和终端标识
> - 更改数据库中的密码和Token

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230417974.png" alt="image-20231102230417974" style="zoom: 50%;" />



#### 4.2 买家功能

买家的基本功能有：下单、支付、取消订单、收货、充值和查询订单等

具体功能代码见be/model/buyer.py

> 需求分析及后端逻辑
>
> - 充值
>   - 更新余额
>   - 更新数据库操作结果

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230606238.png" alt="image-20231102230606238" style="zoom: 50%;" />

> - 下单
>   - 生成订单id
>   - 遍历书籍列表、检查库存
>   - 创建订单详情和记录

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230541338.png" alt="image-20231102230541338" style="zoom: 50%;" />

> - 付款
>
>   - 验证订单有效性
>
>   - 检查订单状态是否未支付
>
>   - 验证用户信息及余额
>
>   - 计算订单总价
>
>   - 更新买家余额和订单状态

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230554530.png" alt="image-20231102230554530" style="zoom:60%;" />



#### 4.3 卖家功能

卖家部分的基本功能有：创建店铺、增加库存和书籍类别、发货和查询订单等。

具体功能代码见be/model/seller.py

> - 创建店铺
>   - 检查店铺Id是否唯一
>   - 插入店铺记录

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230712782.png" alt="image-20231102230712782" style="zoom: 50%;" />







> - 添加书籍
>   - 检查书籍唯一性
>   - 解析书籍信息

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230656300.png" alt="image-20231102230656300" style="zoom:50%;" />

> 增加库存
>
> - 检查书籍是否存在
> - 更新库存

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102230705881.png" alt="image-20231102230705881" style="zoom: 50%;" />







### 后40%进阶功能

> 需求分析

​	按照本次项目提供的功能模块，用户想要买书时，原生支持的操作仅仅只有下单以及付款，并在用户完成付款操作后自动删除订单信息。

​	在实际场景中，在线购买书籍的过程却远远比这复杂许多。为了更好地模拟真实的电商场景，本小组实现需要额外实现一些功能，经过需求分析与组内讨论，新增**书籍发货收货功能、书籍搜索功能、订单的查询与取消功能以及相似书籍推荐**这四个额外的功能模块。

​	具体功能代码见be/model/operations.py，接口代码见be/view/operations.py

#### 4.4 收货&发货

> 后端逻辑
>
> - 发货
>   - 检查订单是否存在
>   - 查询订单详情及状态
>   - 执行发货
>
> - 收货
>   - 验证订单状态
>   - 执行收货

​	为new_order_detail表中引入**订单状态编码state**，以及四个相应状态的**时间戳字段（下单时间、付款时间、发货时间与收货时间）**，并向new_order表中引入了付款时间字段。修改下单和付款操作的代码逻辑，使得用户在完成每个操作后都会造成订单状态的改变。

​	例如从已下单至已付款等，付款后订单不会被自动删除，转入已付款状态。

​	开放商户发货，在商户完成发货后，用户可以执行收货操作。具体来说：

- 用户**下单后**产生订单信息，存储在new_order表与new_order_detail表中。在new_order_detail表中将state置为0（已下单未付款状态），将order_time字段记录为当前的系统时间戳，而其它的三个时间戳（payment_time, delivery_time和receipt_time）被置空。对于new_order表，payment_time字段被置空。
- 用户**付款**后，更新new_order_detail表，设置state字段为1（已付款未发货），并将payment_time字段设为当前的系统时间戳；对于new_order表，同样设置payment_time字段未当前的系统时间戳。
- 商家**发货**后，设置new_order_detail表中的state字段为2（已发货未收货），并将delivery_time字段设为当前系统时间戳。
- 用户**收货**后，设置new_order_detail表中的state字段为3（已收货），并将receipt_time字段设为当前系统时间戳。

​	在实现上述基本流程时，代码还进行了许多操作正确性验证，以确保系统运行的鲁棒性、避免出现未知错误。例如，只有商家可以发货，只有用户可以点击收货等等。

​	在测试中，某笔订单在完成商家发货后，对应的new_order表数据以及new_order_detail字段如下：

![img](file:///C:\Users\86133\AppData\Local\Temp\ksohtml19296\wps1.jpg) 

对于上图的订单，在完成用户收货后，对应的表项如下：

![img](file:///C:\Users\86133\AppData\Local\Temp\ksohtml19296\wps2.jpg) 



#### 4.5 搜索图书

> 后端逻辑
>
> - 全站搜索
>   - 验证搜索关键词
>   - 执行查询
>   - 返回结果
>
> - 当前店铺搜索
>   - 检查搜索关键词
>   - 确认店铺存在
>   - 执行搜索

​	允许用户根据某些关键词去搜索自己感兴趣的书籍很有必要，因此我们引入书籍搜索模块。但是由于数据库中数据量较大，传统的搜索方式会消耗大量的时间，使用mongodb的全文索引来加速书籍搜索的过程，在book表的title、book intro、content以及tags字段均添加了全文索引，然后便可以根据关键词在这四个字段上进行搜索。

​	项目中提供两种搜索模式，分别是**全局搜索以及当前店铺搜索**，前者会搜索数据库中存在的所有书籍，而后者仅仅在当前店铺的书籍中进行搜索。同时，为提升搜索效率，引入了**分页策略**，使得每次搜索最多只会返回10条符合条件的书籍。具体的代码实现见项目目录下的be/model/operations.py下的global_search与local_search函数，并以如下格式返回搜索结果：

“标题: xxx, 作者:xxx, 介绍: xxx, 出版年份:xxx”。

以“撒哈拉”为关键词的全局搜索结果如下，前端仅需处理返回的json信息，即可呈现书籍的标题、作者、介绍、出版年份信息：

<img src="C:\Users\86133\Documents\WeChat Files\wxid_1rpok6jvemqm22\FileStorage\Temp\fa17a65baca9f0d01ac092afaa9de3a.png" alt="fa17a65baca9f0d01ac092afaa9de3a" style="zoom:150%;" />



#### 4.6 订单

> 后端逻辑
>
> - 查询订单
>   - 判断订单是否存在
>   - 执行查询
>
> - 删除订单
>   - 查询订单状态
>     - 未付款（状态为0），则可以直接取消
>     - 已付款但未发货（状态为1），则需要执行退款流程。
>   - 删除订单
>     - 对于未付款订单，直接从订单详情和订单记录中删除订单，并调整库存。
>     - 对于已付款但未发货的订单，除了删除订单和调整库存外，还需要从卖家账户扣除相应金额并退款给买家。
>     - 如果订单已发货或已收货（状态大于1），则不能取消。

​	为更加贴合实际使用场景，引入对订单的查询以及取消机制。查询机制允许用户或者商户查询详细的订单信息，而订单取消机制允许用户取消处于“已下单未付款”状态以及“已付款未发货”状态的订单。

​	订单查询功能会先进行一次用户验证，仅允许当前订单的发起者（即购买书籍的用户）或当前订单的商户进行查询，其它用户的查询将被拒绝并返回错误信息。当查询成功时，返回订单的详细信息。

**订单取消功能的三种情况**

- 订单处于已下单但未付款的状态时，用户可以发起取消订单的操作。此操作只能由下单的用户发起，其它用户的访问将被拒绝。当操作成功后，系统会释放当前订单中的书籍资源，使得这部分书籍可以重新被其它用户购买。
- 订单已经付款，但是商家还未发货，此时同样可以执行退款。除了上述的释放书籍资源外，此时还需要额外执行退款，即商家需要把商品款项退还给用户。
- 订单已经发货或已经收货，此时不允许取消订单。

​	在完成上述逻辑的同时，在模块中引入了大量的异常处理机制，用于针对实际场景中可能出现的各种异常或错误，并针对情况做出反应。例如：当需要退款时，如果商户的余额不足，无法支持此次退款操作时，订单取消操作将被拒绝，并返回相应的错误信息。

​	除此之外，在new_order表以及new_order_detail表的payment_time字段上引入了TTL索引，当payment_time为空（即用户已下单但未付款）且下单时间超过一小时，订单会自动取消。



#### 4.7 推荐

​	受淘宝等实际电商平台的启发，引入相似书籍推荐模块，不改变上述数据表设计的条件下，根据用户历史订单推荐相似的书籍。

​	由于本项目属于课程项目，缺乏实际的用户信息，因此传统的推荐算法（例如协同过滤），均无法有效应用于本项目，故考虑引入一种基于规则的推荐系统，根据书籍的作者以及标签来继续推荐，具体来说，会根据书籍的作者推荐三本同作者的书籍、再根据书籍的标签推荐七本标签类似的书籍。

​	首先获取用户的所有历史订单，并从订单中提取出用户购买的所有书籍，获取作者列表以及标签列表，最后利用全文索引在数据库中进行检索，寻找包含对应关键词的书籍。

​	值得注意的是，由于数据库中存在大量的重复书籍（书实际上是相同，但是由于出版社，出版年份，价格等其它因素，被归为了不同的书籍），且上述策略会查询到用户当前购买的书。因此推荐过程中额外需要维护selected_ids列表与selected_names列表，分别用于存储已经被选中的书籍的book_id与书名，推荐过程中会保证只有book_id和书名没有出现在selected_ids和selected_names的书籍才会被推荐。这样的操作可以保证同一本书不会被多次推荐，且用户购买过的书不会被推荐。

>  某次用户推荐的结果如下，每一项结果会以“标题：xxx, 作者:xxx, 介绍:xxx”的格式被返还，只需解析后便可正常呈现：

![img](file:///C:\Users\86133\AppData\Local\Temp\ksohtml19296\wps4.jpg)

### 发送请求

具体代码见fe/access/operations.py，每个函数会发送HTTP请求到指定的URL进行操作，并返回响应的状态码。

具体说明如下：

**`set_delivery(self, order_id, store_id, store_owner_id, password)`：发货**

- 参数：
  - order_id: 订单ID
  - store_id: 商店ID
  - store_owner_id: 卖家ID
  - password: 卖家密码
- 返回值：HTTP响应的状态码

**`set_receipt(self, order_id, user_id, password)`：收货**

- 参数：
  - order_id: 订单ID
  - user_id: 买家ID
  - password: 买家密码
- 返回值：HTTP响应的状态码

**`order_lookup(self, order_id, user_id, password)`：查询**

- 参数：
  - order_id: 订单ID
  - user_id: 用户ID
  - password: 用户密码
- 返回值：HTTP响应的状态码

**`order_cancer(self, order_id, user_id, password)`：取消订单**

- 参数：
  - order_id: 订单ID
  - user_id: 用户ID
  - password: 用户的密码
- 返回值：HTTP响应的状态码

**`book_search(self, keyword, how, store_id="")`：搜索**

- 参数：
  - keyword: 搜索关键词
  - how: 搜索类型，如全局搜索或本地搜索
  - store_id (可选): 商店ID，在本地搜索时需要提供
- 返回值：HTTP响应的状态码

**`book_recommend(self, user_id, password)`：推荐**

- 参数：
  - user_id: 用户ID
  - password: 用户的密码
- 返回值：HTTP响应的状态码

​	以上的接口函数都会根据传入的参数构造JSON数据，并使用requests库发送POST请求到指定的URL。返回的状态码表示请求的成功与否，可以根据状态码进行相应的处理。

### 基于flask的API接口实现

​	具体代码见be/view/operations.py, 通过解析HTTP请求的JSON数据，调用`operations.Operations`类中相应的函数来处理请求，并将处理结果以JSON格式进行返回。返回的响应中包含一个消息(message)和状态码(code)。

```
卖家发货：通过POST请求发送`/operations/delivery`接口，传入订单ID、商店ID、商店拥有者ID和密码
买家收货：通过POST请求发送`/operations/receipt`接口，传入订单ID、用户ID和密码
买家查询订单：通过POST请求发送`/operations/lookup`接口，传入订单ID、用户ID和密码
取消订单：通过POST请求发送`/operations/cancer`接口，传入订单ID、用户ID和密码
搜索书籍：通过POST请求发送`/operations/search`接口，传入关键词和搜索类型（全局搜索或局部搜索），实现书籍的搜索操作。如果是局部搜索，则需要同时传入商店ID。
相似推荐：通过POST请求发送`/operations/recommend`接口，传入用户ID和密码，实现书籍的相似推荐。根据用户历史订单，基于作者和标签进行推荐。
```

## 五. 测试

> 测试预设和初始化

​	在每个测试用例运行之前，自动执行预设和初始化操作。这包括实例化操作对象，注册买家和卖家，创建一个storeI_id，并在商店中添加一些书籍，方便后续测试其他功能。

初始化样例如图所示：

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105150357651.png" alt="image-20231105150357651" style="zoom:50%;" />

### 5.1 测试接口和样例

**注：测试fe/view/operations.py、be/model/operations.py中的所有函数以及绝大部分可能的error**

#### 5.1.1 发货&收货 test_delivery_receipt.py

**测试逻辑**

> 主要测试交付收据功能的正确性，包括通 过接口和直接调用两种方式。

步骤如下：

1. 生成购买图书信息并下单；
2. 确认订单状态为已支付；
3. 设置交付；
4. 设置收据；
5. 验证设置交付和收据的操作是否成功。

​	**共计8个测试，其中涉及访问接口以及直接访问，仅在报告中展示部分测试函数，具体内容查看fe/test/test_delivery_receipt.py**

**测试用例**

```
test_set_delivery_ok：通过接口设置交付功能，验证交付设置
test_set_delivery_directly_ok：通过直接调用设置交付功能，验证交付设置
test_set_receipt_ok：通过接口设置收据功能，验证收据设置
test_set_receipt_directly_ok：通过直接调用设置收据功能，验证收据设置
test_set_delivery_before_payment：在支付之前设置交付功能，验证是否会返回错误码
test_set_delivery_before_payment_directly：在支付之前直接调用设置交付功能，验证是否会返回错误码
test_set_receipt_before_payment：在支付之前设置收据功能，验证是否会返回错误码
test_set_receipt_before_payment_directly：在支付之前直接调用设置收据功能，验证是否会返回错误码
```

#### 5.1.2 搜索 test_searchbook.py

**测试逻辑**

​	**用户可以通过关键字搜索，参数化的搜索方式；如搜索范围包括，题目，标签，目录，内容；全站搜索或是当前店铺搜索。如果显示结果较大，需要分页(使用全文索引优化查找)**

> 全站搜索在be/model/operations.py中对应global_search函数
>
> 当前店铺搜索在be/model/operations.py中对应local_search函数

- **global_search全局搜索**
  - 如果不输入搜索需要的关键词，则返回914
  - 如果输入了关键词但是没有找到相关内容，则返回915
  - 输入关键词并且查找成功则返回200

- **local_search局部搜索**
  - 如果不输入搜索需要的关键词，则返回914
  - 如果输入了关键词但是没有找到相关内容，则返回915
  - 如果未输入店铺_id或者输入的店铺_id不存在或者店铺里没有任何在售书籍，则返回916
  - 上述错误都不存在则返回200

> search_book方法

![image-20231105150421135](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105150421135.png)

​	用于在所有商店中全局搜索书籍，或者在特定商店内部进行本地搜索，具体取决于 how 参数。根据搜索的结果，它会返回不同的状态码。

​	**共计3个测试，其中涉及访问接口以及直接访问，仅在报告中展示部分测试函数，具体内容查看fe/test/test_searchbook.py**

**测试用例**

```
test_global_search：全局搜索功能，包括使用有效、无效关键字和空关键字进行搜索，并验证返回码和书籍列表
test_local_search：本地搜索功能，包括使用有效关键字和空关键字进行搜索，并验证返回码和书籍列表
test_local_search_without_store_id：未提供商店ID时的本地搜索功能，包括使用有效关键字、不存在的关键字和存在的关键字进行搜索，并验证返回码和书籍列表
```

#### 5.1.3 订单 test_order.py

**测试逻辑**

​	从创建订单、查询订单、删除订单以及卖家和买家等多个方面对功能进行测试：创建订单、删除不存在的订单、下单后查询订单、查询不存在的订单、发货后查询订单、收货后查询订单、下单未付款删除订单、下单并且付款之后删除订单等等。

**测试用例**

​	**共计14个测试，其中涉及访问接口以及直接访问，仅在报告中展示部分测试函数，具体内容查看fe/test/test_order.py**

```python
test_cancel_order_ok(self):测试删除订单正常
test_cancel_non_exist_buyer_id(self):当买家id不存在时，测试删除订单，正确结果是无法删除
test_cancel_non_exist_buyer_direct_id(self):买家id不存在时，直接访问后端删除订单，正确结果是无法删除
test_cancel_non_exist_order_id(self):订单id不存在时，测试删除该订单。
test_processing_order(self): 下单后查询当前订单
test_processing_order_sent(self):发货后查询当前订单
test_processing_order_sent_error(self): 因为各种错误发货失败
test_sent_order_direct_cancer(self):发货后删除当前订单
test_processing_order_receive(self):收货后查询当前订单
test_processing_order_receipt_error(self): 因为各种错误收货失败
test_seller_processing_order_ok(self):卖家查询订单
```

#### 5.1.4 测试推荐

**测试逻辑**

1. 进行测试前的初始化操作；
2. 生成购买图书信息并下单；
3. 验证订单是否成功创建；
4. 进行推荐书籍的操作；
5. 验证推荐书籍操作的返回码。

**测试用例**

​	**共计6个测试，其中涉及访问接口以及直接访问，仅在报告中展示部分测试函数，具体内容查看fe/test/test_recommend.py**

```
test_recommend_ok：通过接口推荐书籍，并验证返回码
test_recommend_ok_directly：直接调用进行推荐书籍操作，并验证返回码
test_recommend_authorization_fail：通过接口进行推荐书籍操作时，验证授权失败的情况
test_recommend_authorization_fail_directly：直接调用进行推荐书籍操作时，验证授权失败的情况
test_recommend_no_order_fail：测试没有下过订单的情况下进行推荐书籍操作，验证返回码
test_recommend_no_order_fail_directly：测试没有下过订单的情况下直接调用进行推荐书籍操作，验证返回码
```

### 5.2 测试结果截图

![image-20231102224317113](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102224317113.png)

![image-20231102224342371](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102224342371.png)

![image-20231102142420483](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102142420483.png)

共计61个测试用例，全部通过

![image-20231102224502493](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102224502493.png)

![image-20231102224602035](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102224602035.png)

![image-20231102224625031](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102224625031.png)

**紫色**：后40%要求的功能函数所在的文件，其中access给view发送请求，view转送给model处理请求，将处理结果返回给access。【100%】

**白色**: 整体覆盖率【75%】

- ​	部分be/model/buyer.py函数在be/model/operations.py中有重复，仅测试be/model/operations.py当中的功能，因此buyer.py覆盖率降低

**蓝色**：后端测试代码

- 新增功能代码：
  - be/model/operations.py: 功能
  - be/view/operations.py:后端接口
  - fe/access/operations.py: 发送请求

- 新增测试代码：
  - fe/test/test_delivery_recipt.py:测试收货和发货
  - fe/test/test_booksearch.py:测试书本的搜索（全局和局部）
  - fe/test/test_order.py:测试订单（删除和搜索以及状态）
  - fe/test/test_recommend:测试推荐功能

### 5.3 Postman测试

==注：由于测试结果在上述内容中已经展示，如下测试截图仅展示部分功能，表示已进行postman测试并且已拓展应用在后40%功能上。（若要测验后40%功能，需要将前60%功能测试全部进行一遍，postman才会存储买家、卖家、订单以及书本信息）==

#### 前60%：取部分测试截图

**格式**:body选择raw->json

> {
>
>   ​	"user_id":"whatareyounongshalei",
>
>   ​	"password":"1111"
>
> }

> 注册用户：http://127.0.0.1:5000/auth/register

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105153522524.png" alt="image-20231105153522524" style="zoom: 50%;" />

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105153634482.png" alt="image-20231105153634482" style="zoom: 50%;" />

> 注销用户：http://127.0.0.1:5000/auth/unregister

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105153815127.png" alt="image-20231105153815127" style="zoom: 50%;" />

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105153849949.png" alt="image-20231105153849949" style="zoom:50%;" />

> 用户登录：http://127.0.0.1:5000/auth/login

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105154847963.png" alt="image-20231105154847963" style="zoom:50%;" />



> 更改密码：http://127.0.0.1:5000/auth/password

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105155304593.png" alt="image-20231105155304593" style="zoom:50%;" />

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105155407301.png" alt="image-20231105155407301" style="zoom:50%;" />

> 买家下单：http://127.0.0.1:5000/buyer/new_order

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105160736514.png" alt="image-20231105160736514" style="zoom:50%;" />

> 买家充值：http://127.0.0.1:5000/buyer/add_funds

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105161618404.png" alt="image-20231105161618404" style="zoom:50%;" />

#### 后40%:仅展示与订单相关

> 发货：http://127.0.0.1:5000/operations/delivery

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105164921437.png" alt="image-20231105164921437" style="zoom:50%;" />

> 收货：http://127.0.0.1:5000/operations/receipt

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105165103022.png" alt="image-20231105165103022" style="zoom:50%;" />

> 查找订单：http://127.0.0.1:5000/operations/lookup

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105165328259.png" alt="image-20231105165328259" style="zoom:50%;" />

> 取消订单：http://127.0.0.1:5000/operations/cancer

<img src="C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105165454378.png" alt="image-20231105165454378" style="zoom:50%;" />

## 六. 遇到的问题

1.  `requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`

Q：① 传入接口的数据类型以及所需参数数量保持一致

​       ② 切换解释器至3.12及以上版本，重新配置环境

2. `assert 905 == 200`

Q：查看后端部分设置每种状态的返回值，与测试时返回的状态码保持一致。

3. `RuntimeError: Not running with the Werkzeug Server`

Q：flask版本太高，需要降低版本

```python
pip install flask==2.0.0  
pip install Werkzeug==2.0.0
```

4. `起初不知道如何测试店铺id存在并且有效的情况，并且使用self.store_id一直显示916，即输入的店铺_id不存在`

   ![image-20231105145702974](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105145702974.png)

   Q: 在实例化操作对象后，自己手动创建一个store_id为“111”的商店并且命名为exist_store_id。然后手动往商店中添加书籍。在后续的测试中一律把self.store_id替换成self.exist_store_id

   ![image-20231105145735823](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105145735823.png)

5. `在从fe.access模块导入operations后，想将接口的book_search函数在测试中细化成global_search和local_search两个部分`

   Q: 新增函数search_books

   ![image-20231105145843974](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231105145843974.png)

   代码将调用 self.opera（前面创建的 operations.Operations 实例）的 book_search 方法来执行搜索。此方法将根据指定的 keyword 进行搜索，并根据 how 参数是 "global_search" 还是 "local_search" 来决定是否需要传递 store_id。

## 七. 项目亮点

### 7.1 使用git版本管理工具

github仓库地址：https://github.com/Airthe911/DataBase_Project1

github仓库SSH：git@github.com:Airthe911/DataBase_Project1.git

github工作流截图如下

![282078f54b381245fb9de552de4a876](C:\Users\86133\Documents\WeChat Files\wxid_1rpok6jvemqm22\FileStorage\Temp\282078f54b381245fb9de552de4a876.png)

![bc7d582479f65adef1b856158d60c04](C:\Users\86133\Documents\WeChat Files\wxid_1rpok6jvemqm22\FileStorage\Temp\bc7d582479f65adef1b856158d60c04.png)

### 7.2 索引

> 搜索图书

- 使用：使用MongoDB的全文索引功能，通过"$text"运算符来指定进行文本搜索的字段，优化文本搜索的性能。
- 实现方式：首先判断关键词是否为空，如果为空则返回错误码914，表示搜索关键词不能为空。然后，通过在指定字段上执行文本搜索，使用"$search"运算符指定搜索关键词。通过调用find方法进行搜索，并限制结果数量为10条。如果搜索结果为空，则返回错误码915，表示没有找到相关内容。如果搜索结果不为空，则将搜索结果按照指定格式拼接成字符串并返回结果。
- 功能说明：“索引”在这里起到了加快搜索速度的作用。通过在指定字段上建立索引，MongoDB可以更快地定位到符合搜索条件的数据。

### 7.3 推荐功能

![image-20231102225858916](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231102225858916.png)

​	**接受用户的身份验证信息，根据用户的历史订单推荐用户可能感兴趣的书籍。**

​	这个功能的主要用处是**为用户提供个性化的推荐**，根据用户的历史订单了解用户的偏好，推荐与用户兴趣相关的书籍，帮助用户发现更多可能感兴趣的内容。

​	使用此功能的条件是**用户必须登录，并提供正确的账号和密码**。**用户必须有历史订单，否则无法进行推荐**。如果用户的账号或密码错误，或者用户没有历史订单，将会返回相应的错误信息。

## 八. 分工与合作

李嘉豪: 后端功能+收发货测试+推荐功能测试

杨茜雅：数据库转换+搜索测试+需求分析

王溢阳：ER图+订单测试+Postman测试

数据库设计：全员

项目报告：全员