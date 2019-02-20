
#一级类型
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10001, '女装 / 男装 / 内衣', 'static/imgs/goods/aaa.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10002, '鞋靴 / 箱包 / 配件', 'static/imgs/goods/aaa.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10003, '童装玩具 / 孕产 / 用品', 'static/imgs/goods/aaa.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10004, '家电 / 数码 / 手机', 'static/imgs/goods/aaa.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10005, '美妆 / 洗护 / 保健品', 'static/imgs/goods/aaa.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10006, '珠宝 / 眼镜 / 手表', 'static/imgs/goods/aaa.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10007, '运动 / 户外 / 乐器', 'static/imgs/goods/aaa.png', '', null);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(10008, '游戏 / 动漫 / 影视', 'static/imgs/goods/aaa.png', '', null);


#二级类型
#1女装 / 男装 / 内衣
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100001, '袜子', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100002, '衬衫', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100003, '西裤', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100004, 'T桖', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100005, '牛仔裤', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100006, '连衣裙', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100007, '丝袜', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100008, '睡裙', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100009, '秋裤', 'static/imgs/goods/aaa.png', '', 10001);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(100010, '毛衣', 'static/imgs/goods/aaa.png', '', 10001);



#2鞋靴 / 箱包 / 配件
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200001, '女鞋', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200002, '红人同款', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200003, '夏上新', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200004, '一脚蹬' , 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200005, '平底鞋', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200006, '复古方头', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200007, '爸爸鞋', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200008, '正装商务', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200009, '增高鞋', 'static/imgs/goods/aaa.png', '', 10002);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(200010, '豆豆鞋', 'static/imgs/goods/aaa.png', '', 10002);



#3童装玩具 / 孕产 / 用品
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300001, '亲子玩具', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300002, '女童外套', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300003, '遮阳帽', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300004, '亲子装' , 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300005, '玩具', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300006, '积木', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300007, '早教', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300008, '儿童自行车', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300009, '户外玩具', 'static/imgs/goods/aaa.png', '', 10003);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(300010, '描红本', 'static/imgs/goods/aaa.png', '', 10003);



#4家电 / 数码 / 手机
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400001, '蒸汽拖把', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400002, '除螨仪', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400003, '吸尘器', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400004, '豆浆机' , 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400005, '足浴盆', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400006, '卷发器', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400007, '蓝牙音箱', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400008, '看戏机', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400009, '油烟机', 'static/imgs/goods/aaa.png', '', 10004);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(400010, '厨房大电', 'static/imgs/goods/aaa.png', '', 10004);



#5美妆 / 洗护 / 保健品
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500001, '蒸汽拖把', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500002, '除螨仪', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500003, '吸尘器', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500004, '豆浆机' , 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500005, '足浴盆', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500006, '卷发器', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500007, '蓝牙音箱', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500008, '看戏机', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500009, '油烟机', 'static/imgs/goods/aaa.png', '', 10005);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(500010, '厨房大电', 'static/imgs/goods/aaa.png', '', 10005);



#6珠宝 / 眼镜 / 手表
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600001, '珍珠', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600002, '金镶玉', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600003, '钻石', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600004, '岫岩玉雕' , 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600005, '翡翠玉石', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600006, '设计师', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600007, '珠宝首饰', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600008, '金条', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600009, '情侣对戒', 'static/imgs/goods/aaa.png', '', 10006);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(600010, '琥珀原石', 'static/imgs/goods/aaa.png', '', 10006);



#7运动 / 户外 / 乐器
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700001, '大Air皮蓬', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700002, 'Kayano2', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700003, '阿迪达斯', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700004, '亚瑟士' , 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700005, '匡威', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700006, '彪马', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700007, 'VANS', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700008, '斯凯奇', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700009, '美津浓', 'static/imgs/goods/aaa.png', '', 10007);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(700010, '健身', 'static/imgs/goods/aaa.png', '', 10007);



#8游戏 / 动漫 / 影视
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800001, 'DNF', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800002, '魔兽', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800003, '坦克世界', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800004, '街头篮球' , 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800005, '大话西游2', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800006, '倩女幽魂', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800007, '冒险岛', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800008, '问道', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800009, '大唐无双', 'static/imgs/goods/aaa.png', '', 10008);
INSERT INTO goods_goodstype(id, name, cover, intro, parent_id) values(800010, '龙之谷', 'static/imgs/goods/aaa.png', '', 10008);












