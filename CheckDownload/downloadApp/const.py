# -*- coding: utf-8 -*-
class GenderFlag():
    FLAG_MALE = 0
    FLAG_FEMALE = 1
    CHOICES = (
                (FLAG_MALE,u'男'),
                (FLAG_FEMALE,u'女')
              )
    
class CustomerFlag():
    FLAG_MEM = 0
    FLAG_MEM_GOLD = 1
    FLAG_MEM_PLATINUM = 2
    FLAG_MEM_DIAMOND = 3
    FLAG_MEM_BLACK_DIAMOND = 4
    CHOICES = (
                (FLAG_MEM,u'会员'),
                (FLAG_MEM_GOLD,u'金卡会员'),
                (FLAG_MEM_PLATINUM,u'白金会员'),
                (FLAG_MEM_DIAMOND,u'钻石会员'),
                (FLAG_MEM_BLACK_DIAMOND,u'黑钻会员'),
               )
    
class ContentFlag():
    FLAG_LIQUOR = 0
    FLAG_TEA = 1
    FLAG_CATERING_FOOD = 2
    FLAG_REGIMEN = 3
    FLAG_BUSINESS = 4
    FLAG_ENTERTAIN = 5
    FLAG_ART = 6
    FLAG_PERSONAL_JEWELS = 7
    FLAG_PERSONAL_TRAVEL = 8
    FLAG_CLUB = 9
    CHOICES = (
                (FLAG_LIQUOR,u'名酒'),
                (FLAG_TEA,u'品茗'),
                (FLAG_REGIMEN,u'养生保健'),
                (FLAG_BUSINESS,u'商务'),
                (FLAG_ENTERTAIN,u'娱乐'),
                (FLAG_ART,u'艺术品'),
                (FLAG_CLUB,u'会所'),
                (u'私人订制',(
                      (FLAG_PERSONAL_JEWELS,u'私人订制珠宝'),
                      (FLAG_PERSONAL_TRAVEL,u'私人订制旅游'),        
                    )
                 ),
                (u'餐饮',(
                     (FLAG_CATERING_FOOD,u'餐饮食品'),
                    )
                 ),
             )
    
class ArticleFlag():
    FLAG_LIQUOR = 0
    FLAG_TEA = 1
    FLAG_CATERING = 2
    FLAG_REGIMEN = 3
    FLAG_BUSINESS = 4
    FLAG_PERSONAL = 5
    FLAG_CLIENT = 6
    FLAG_ENTERTAIN = 7
    FLAG_SHOW = 8
    FLAG_CLUB = 9
    FLAG_MEMBER = 10
    FLAG_AUTHOR = 11
    FLAG_WEALTH_SUPPLY = 12
    FLAG_WEALTH_NEED = 13
    CHOICES = (
                (FLAG_LIQUOR,u'名酒'),
                (FLAG_TEA,u'品茗'),
                (FLAG_CATERING,u'餐饮'),
                (FLAG_REGIMEN,u'养生保健'),
                (FLAG_BUSINESS,u'多功能厅'),
                (FLAG_PERSONAL,u'私人订制'),
                (FLAG_CLIENT,u'客户服务'),
                (FLAG_ENTERTAIN,u'娱乐'),
                (FLAG_SHOW,u'视频展示'),
                (FLAG_CLUB,u'了解我们'),
                (FLAG_MEMBER,u'会员简章'),
                (FLAG_AUTHOR,u'作者简介'),
                (FLAG_WEALTH_SUPPLY,u'财富供应'),
                (FLAG_WEALTH_NEED,u'财富需求'),
             )
    
class ArticleSubFlag():
    FLAG_PEARL = 0
    FLAG_MEMORIAL = 1
    FLAG_GIFT = 2
    FLAG_HOUSEKEEPER = 3
    FLAG_ASSISTANCE = 4
    CHOICES = (
                (FLAG_PEARL,u'珠宝、皮带、服装、皮鞋'),
                (FLAG_MEMORIAL,u'个人高端纪念品'),
                (FLAG_GIFT,u'企业礼包定制'),
                (FLAG_HOUSEKEEPER,u'私人管家定制'),
                (FLAG_ASSISTANCE,u'私人商务助理'),
             )
    
class ServiceFlag():
    FLAG_PEARL = 0
    FLAG_MEMORIAL = 1
    FLAG_GIFT = 2
    FLAG_HOUSEKEEPER = 3
    FLAG_TICKET = 4
    FLAG_TRAVEL = 5
    FLAG_ASSISTANCE = 6
    FLAG_PERSONAL = 7
    CHOICES = (
                (FLAG_PEARL,u'珠宝、皮带、服装、皮鞋'),
                (FLAG_MEMORIAL,u'个人高端纪念品'),
                (FLAG_GIFT,u'企业礼包定制'),
                (FLAG_HOUSEKEEPER,u'私人管家定制'),
                (FLAG_TICKET,u'机票预订'),
                (FLAG_TRAVEL,u'旅游团预订'),
                (FLAG_ASSISTANCE,u'商务助理'),
                (FLAG_PERSONAL,u'私人商务助理介绍'),
             )
    
                