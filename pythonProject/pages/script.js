function handleLogin() {
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;

    // 创建一个 FormData 对象来存储要发送的数据
            var formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);

    // 使用 Fetch API 发送 POST 请求
            fetch('http://139.196.202.40:8800/api/login', {
             method: 'POST',
             body: formData,
            })
            .then(response => {
        // 检查响应状态码
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // 解析 JSON 数据
        })
        .then(data => {
        // 假设后端返回的数据中有一个 `success` 字段表示登录是否成功
        if (data.status === 'success') {
            document.getElementById("loginPage").style.display = "none";
            document.getElementById("tabs").style.display = "flex";
            uid = data.uid; // 保存用户 ID
            sessionStorage.setItem('userUid', uid);
            const expiryTime = new Date().getTime() + 1 * 60 * 1000; // 毫秒
            console.log(expiryTime); // 保存用户 ID 到 sessionStorage
            sessionStorage.setItem('userUidExpiry', expiryTime.toString());
            const myTab = document.getElementById('myTab');  
            const orderTab = document.getElementById('orderTab');
            const myContent = document.getElementById('myContent');
            const orderContent = document.getElementById('orderContent');
  
    // 移除所有tab上的active类  
            myTab.classList.remove('active');  
            orderTab.classList.add('active'); // 给订单tab添加active类 
            myContent.classList.remove('active');
            orderContent.classList.add('active');
            getTodayOrders(); // 调用"今日下单"接口获取最新数据


            // changeTab('order'); // 登录成功后默认显示“下单”页面
        } else {
            alert("用户名或密码错误");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("登录失败，请重试");
    });

    // 阻止表单的默认提交行为
    return false;
        }
        

function changeTab(tabId) {
            var contents = document.getElementsByClassName('content');
            for (var i = 0; i < contents.length; i++) {
                contents[i].classList.remove('active');
            }
            document.getElementById(tabId).classList.add('active');
            if (tabId === 'order') {
                getTodayOrders(); // 调用"今日下单"接口获取最新数据
            }
           //  if (tabId === 'my') {
           //  fetchMyHistoryOrders();
           // }
}



document.addEventListener('DOMContentLoaded', function() {  
    const tabs = document.querySelectorAll('.tab-button');  
    const contents = document.querySelectorAll('.content-container');  
  
    tabs.forEach(tab => {  
        tab.addEventListener('click', function() {  
            // 移除所有tabs和内容容器的active类  
            tabs.forEach(t => t.classList.remove('active'));  
            contents.forEach(c => c.classList.remove('active'));  
  
            // 添加当前点击的tab和内容容器的active类  
            this.classList.add('active');  
            document.getElementById(this.id.replace('Tab', 'Content')).classList.add('active');  
        });  
    });  
});
    

function fetchMyHistoryOrders(event) {  
    var uid = sessionStorage.getItem('userUid');
    

    const expiryTimeStr = sessionStorage.getItem('userUidExpiry');
    const expiryTime = new Date(parseInt(expiryTimeStr));
    if (new Date().getTime() > expiryTime.getTime()) {
        console.log("登录已过期");
        alert("您的登录会话已过期，请重新登录。");

        sessionStorage.removeItem('userUid');
        sessionStorage.removeItem('userUidExpiry');
        window.location.href = "index.html";
        return; // 退出函数，因为用户需要重新登录
    }
    // event.preventDefault(); // 阻止表单的默认提交行为  
  
    // 获取表单数据  
    const formData = new FormData(document.getElementById('historyOrdersForm'));  
  
    // 发送POST请求到服务器  
    fetch('http://139.196.202.40:8800/api/history-orders', { // 注意：这里应该是'history-orders'而不是'today-orders'  
        method: 'POST',  
        body: formData,  
    })  
    .then(response => {  
        if (!response.ok) {  
            throw new Error('Network response was not ok');  
        }  
        return response.json();  
    })  
    .then(data => {  
        // 假设返回的数据中有一个'data'字段包含订单数组  
        var orders = data.data || []; // 如果没有数据，则默认为空数组  
        var historyOrdersResult = document.getElementById('historyOrdersResult');  
  
        // 清空旧内容  
        historyOrdersResult.innerHTML = '';  
  
        // 如果订单数组不为空，则生成表格并显示  
        if (orders.length > 0) {  
            var table = document.createElement('table');  
            var thead = document.createElement('thead');  
            var tbody = document.createElement('tbody');  
  
            // 创建表头  
            var headerRow = document.createElement('tr');  
            ['订单ID', '菜品', '数量', '单位', '单价', '总价'].forEach(headerText => {  
                var th = document.createElement('th');  
                th.textContent = headerText;  
                headerRow.appendChild(th);  
            });  
            thead.appendChild(headerRow);  
  
            // 填充表格体  
            orders.forEach((order, index) => {  
                var row = document.createElement('tr');  
                ['orderId', 'dish', 'quantity', 'danwei', 'price', 'totalPrice'].forEach(key => {  
                    var cell = document.createElement('td');  
                    cell.textContent = order[key] || '未知';  
                    row.appendChild(cell);  
                });  
                tbody.appendChild(row);  
            });  
  
            table.appendChild(thead);  
            table.appendChild(tbody);  
            historyOrdersResult.appendChild(table);  
        } else {  
            // 如果没有订单，则显示消息  
            historyOrdersResult.textContent = '没有找到历史订单。';  
        }  
    })  
    .catch((error) => {  
        console.error('Error fetching history orders:', error);  
        alert('获取历史订单时发生错误，请稍后再试。');  
    });  
  
    // 阻止表单的默认提交并返回false，以便不刷新页面  
    return false;  
}



        function order() {
            var dish = document.getElementById("dish").value;
            var quantity = document.getElementById("quantity").value;
            var uid = sessionStorage.getItem('userUid');
            const expiryTimeStr = sessionStorage.getItem('userUidExpiry');
            const expiryTime = new Date(parseInt(expiryTimeStr));
            if (new Date().getTime() > expiryTime.getTime())
            {
                console.log("登录已过期");
                alert("您的登录会话已过期，请重新登录。");
                sessionStorage.removeItem('userUid');
                sessionStorage.removeItem('userUidExpiry');
                window.location.href = "index.html";
            }

            var formData = new FormData();
            formData.append('dish', dish);
            formData.append('quantity', quantity);
            formData.append('uid', uid);

            fetch('http://139.196.202.40:8800/api/data', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("result").textContent = "下单结果：" + data.msg;
                getTodayOrders(); // 调用"今日下单"接口获取最新数据
                document.getElementById("dish").value = ""; // 清空菜名输入框
                document.getElementById("quantity").value = ""
            })
            .catch((error) => {
                console.error('Error:', error);
            });
            return false;
        }


        function getTodayOrders() {
         var uid = sessionStorage.getItem('userUid');
         var formData = new FormData();
         const expiryTimeStr = sessionStorage.getItem('userUidExpiry');
            const expiryTime = new Date(parseInt(expiryTimeStr));
            if (new Date().getTime() > expiryTime.getTime())
            {
                console.log("登录已过期");
                alert("您的登录会话已过期，请重新登录。");

                sessionStorage.removeItem('userUid');
                sessionStorage.removeItem('userUidExpiry');
                window.location.href = "index.html";
            }
         formData.append('uid', uid);
         fetch('http://139.196.202.40:8800/api/today-orders', { // 注意：这里假设URL是'history-orders'而不是'today-orders'
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        var orders = data.data; // 假设返回的数据中有一个'data'字段包含订单数组
        var table = document.createElement('table'); // 创建一个表格元素
        var thead = document.createElement('thead'); // 表格头部
        var tbody = document.createElement('tbody'); // 表格体

        // 创建表头
        var headerRow = document.createElement('tr');
        // 假设每个订单对象都有'orderId', 'dish', 'quantity'等属性
        ['订单ID', '菜品', '数量','单位','单价', '总价'].forEach(headerText => {
            var th = document.createElement('th');
            th.textContent = headerText;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);

        // 填充表格体
        orders.forEach((order, index) => {
            var row = document.createElement('tr');
            // 假设订单对象具有与表头对应的属性
            ['orderId', 'dish', 'quantity', 'danwei', 'price', 'totalPrice'].forEach(key => {
                var cell = document.createElement('td');
                cell.textContent = order[key] || '未知'; // 如果属性不存在，则显示'未知'
                row.appendChild(cell);
            });
            tbody.appendChild(row);
        });

        table.appendChild(thead);
        table.appendChild(tbody);

        // 假设你有一个元素来放置这个表格，比如<div id="ordersTable"></div>
        document.getElementById("todayOrders").innerHTML = ''; // 清空旧内容（如果有的话）
        document.getElementById("todayOrders").appendChild(table); // 将表格添加到DOM中
    })
    .catch((error) => {
        console.error('Error fetching orders:', error);
        alert('获取订单时发生错误，请稍后再试。');
    });
}

window.onload = function() {
    fetchAndGenerateInputs();
};

function fetchAndGenerateInputs() {
    fetch('http://139.196.202.40:8800/api/dishes')
        .then(response => response.json())
        .then(data => {
            let form = document.getElementById('orderForm');
            data = data.dishes;
            data.forEach(dish => {
                form.innerHTML += `
                    ${dish.name}：<input type="text" id="${dish.id}"><span>(${dish.unit})</span><br>
                `;
            });
        });
}

// 提交订单
function submitOrder() {
    getTodayOrders();
    let order = [];
    let inputs = document.getElementById('orderForm').getElementsByTagName('input');
    for (let i = 0; i < inputs.length; i++) {
        order.push({
            name: inputs[i].id,
            quantity: inputs[i].value,
            unit: '斤' // 单位暂时固定为斤
        });
    }
    fetch('api/submitOrder', { // 假设这个API用来提交订单
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(order)
    });
}