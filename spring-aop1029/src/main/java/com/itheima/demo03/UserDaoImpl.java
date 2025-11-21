package com.itheima.demo03;

public class UserDaoImpl implements UserDao {
    @Override
    public void add() {
        System.out.println("add something in UserDaoImpl");
    }
    @Override
    public void update() {
        System.out.println("update something in UserDaoImpl");
    }
    @Override
    public void delete() {
        System.out.println("delete something in UserDaoImpl");
    }
    @Override
    public void select() {
        System.out.println("select something in UserDaoImpl");
    }
    // alt +enter
}
