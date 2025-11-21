package com.itheima.demo03;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;

public class XmlAdvice {
    public void before1(JoinPoint joinPoint){
        System.out.println("this is before method ");
        System.out.println("the target name is "+ joinPoint.getTarget());
        System.out.println("the target method woven enhanced processing is " + joinPoint.getSignature().getName());
    }
    public void afterReturning1(JoinPoint joinPoint){
        System.out.println("the target method woven enhanced processing is" + joinPoint.getSignature().getName());
    }
    public Object around (ProceedingJoinPoint point) throws  Throwable{
        System.out.println("this is before part of around ");
        Object object = point.proceed();
        System.out.println("this is after part of around ");
        return  object ;
    }
    public void after(){
        System.out.println("the method is after");
    }
    public void afterException(){
        System.out.println("the method is afterException");
    }
}
