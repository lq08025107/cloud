# 什么是Mesos

Apache Mesos abstracts CPU, Memory, storage, and other compute resources away from machines(physical or virtual), enabling fault-tolerant and elastic distributed systems to easily be built and run effectively

# 关键术语

1 Mesos-Master

负责管理各个framework和slave，将slave上的资源分配给framework

2 Mesos-slave

负责管理本节点上的各个mesos-task

3 Framework

计算框架，譬如Hadoop， Spark，通过MesosSchedulerDriver接入Mesos

4 Executor

安装到Mesos-slave，用于启动框架中的task

当用户试图添加一种计算框架到Mesos中时，需要实现一个Framework Scheduler和executor以接入Mesos

# 实战以及记录坑



# Kubernetes

Production-Grade Container Orchestration（Automated container deployment, scaling, and management）

Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit

# Kubernetes和Mesos区别
