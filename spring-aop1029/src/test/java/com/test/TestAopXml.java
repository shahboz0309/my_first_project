package com.test;

import com.itheima.demo03.UserDao;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestAopXml {
    public static void main(String[] args) {
        ApplicationContext applicationContext = new
                ClassPathXmlApplicationContext("applicationContext.xml");
        UserDao userDao = applicationContext.getBean("userDao", UserDao.class);
        userDao.add();
        System.out.println("\n");
        userDao.select();
        System.out.println("\n");
        userDao.update();
        System.out.println("\n");
        userDao.delete();
        System.out.println("\n");
    }
}
