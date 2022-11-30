# The Refrp For Cloud Manager
## 1.Why I make this software
> As everybody know when we want to connect to our site to manage your vps ,the safety is the most importain thing thar you should consider. But the sad news is that we can't connect to our site safely except we use https protrol .But for many people ,they don't have a vilid cert to use for their website ,and if you are useing the China cloud ,you will need to **_beian_** ,but I just want to build a website for my self to control my vps ,and this is the reason why I made this software.
## 2.How this work
>When you start this software both in your local host and the vps, it will build the private tunnel to exchange the message. You can use rsa or base64 to encrypt the message. And it is safe and the cloud won't know what your send in your message.
## 3.How to use
>Choose the encrypt method you need ,and start the soft ware both in your local host and the vps .And type in the message as the software show. 

## **Notice**
>If you need the long connection of the tcp, you need set the time out more loog ,such if you need to use the ssh , I will suggest you turn it to more than 20 second. And if you use it for shot tcp connection you should turn it to 3s such as https or http 
