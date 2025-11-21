package com.itheima.demo03;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;

@Aspect
public class AnnoAdvice {
    // config pointcut
    @Pointcut("execution( * com.itheima.demo03.UserDaoImpl.*(..))")
    public void pointcut(){
    }

    @Before("pointcut()")
    public void before(JoinPoint joinPoint){
        System.out.println("this is before method ");
        System.out.println("the target name is "+ joinPoint.getTarget());
        System.out.println("the target method woven enhanced processing is " + joinPoint.getSignature().getName());
    }

    @AfterReturning("pointcut()")
    public void afterReturning1(JoinPoint joinPoint){
        System.out.println("the target method woven enhanced processing is " + joinPoint.getSignature().getName());
    }
    @Around("pointcut()")
    public Object around (ProceedingJoinPoint point) throws  Throwable{
        System.out.println("this is before part of around ");
        Object object = point.proceed();
        System.out.println("this is after part of around ");
        return  object ;
    }
    @After("pointcut()")
    public void after(){
        System.out.println("the method is after");
    }
    @AfterThrowing("pointcut()")
    public void afterException(){
        System.out.println("the method is afterException");
    }

}
