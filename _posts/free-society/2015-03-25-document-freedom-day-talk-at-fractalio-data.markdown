---
layout: post
title: "Document Freedom Day Talk at Fractalio Data"
modified:
categories: free-society
description: An step of the awareness program initiative by Fractalio Data
tags: [free-society, document-freedom-day, dfd2015, opentalk ]
image:
  feature: true
  credit: Free Software
  creditlink: http://gnu.org
comments: true
share:
date: 2015-03-25T02:11:33-04:00
---

We were happy to celebrate Document Freedom Day 2015 at Fractalio Data. We had a small talk titled  "What is Document Freedom and Why should I care about it". We had about 20 people working in our shared offices come in.

## Event Report :  <br />
25 March 2015 organized by <br />
Event: Open Talk <br />
Date: 25 March 2015 from 11:00 to 11:45  <br />
Place: Fractalio Data shared office space.  <br />

## About the Talk: <br />
This DFD was celebrated along with the birthday of our colluege Ms.Prathiba. We had a cake cutting (for the birthday) which was followed a talk by Ramaseshan.S, along with Kiran Patil, Naveen and Raghuram who are a part of Engineering Team at Fractalio Data. A special thanks to be given to Pradeed of Data Lifecycle Company for helping us get organized. 

This talk basically focussed on the following topics.

1. What is a document
2. Defination of Freedom in documents
3. Why should you be worried if the non-free documents and what are the document standards.
4. Why should you also be a part of Document Freedom movement and start using document standsrds
5. A few examples of open document standards like IP, Libre Office etc.


# Image gallery

<div id="dfd_images">
</div>


**We would like to thank Ms. Sangeetha for organising the event and the participants, and the DatalifeCycle Company for the space. Greater thanks to Ms. Prathiba for allowing us to celebrate DFD along with her birthday. Thanks to all the participants for attending.**

**A special thanks for Free Software Foundation Tamilnadu(FSFTN http://fsftn.org/) and FSF (Free Software Foundation), for the stickers and swags that we used for distributing to the participants. We would also like to thank all the contributers in the Free and Open world, without whom this whole talk would not have been possible.**


<script>
var dir = "/images/dfd-images/";
var fileextension = ".jpg";
$.ajax({
    //This will retrieve the contents of the folder if the folder is configured as 'browsable'
    url: dir,
    success: function (data) {
        //Lsit all png file names in the page
        $(data).find("a:contains(" + fileextension + ")").each(function () {
            var filename = this.href.replace(window.location, "").replace("http:///", "");
            $("#dfd_images").append($("<img src=" + dir + filename + "></img>"));
        });
    }
});
</script>
