#!/usr/bin/python
#-*- coding:utf-8 -*-

from xml.dom import minidom

class SolrXml():
    def __init__(self):
        self.mdoc = minidom.Document()
        self.addNode = self.mdoc.createElement("add")
        self.mdoc.appendChild(self.addNode)

    def create_field(self,key,value):
        field = self.mdoc.createElement("field")
        field.setAttribute("name",key)
        field.appendChild(self.mdoc.createTextNode(value))
        return field

    def create_doc(self):
        doc = self.mdoc.createElement("doc")
        self.addNode.appendChild(doc)
        return doc

    def parse(self,objs):
        for obj in objs:
            doc = self.create_doc()
            for k,v in obj.iteritems():
                if isinstance(v, list):
                    for l in v:
                        field_node = self.create_field(k,l)
                        doc.appendChild(field_node)
                else:
                    field_node = self.create_field(k,v)
                    doc.appendChild(field_node)

if __name__=='__main__':

    objs = [
      {
        "id": "exuntong-button-00001",
        "cat": ["button","app"],
        "name": "满意调查",
        "iconClass_s": "icon-evaluation",
        "pageUrl_s": "pages/evaluation/evaluation",
        "content":  "满意度测评的平台，收集病人的满意度评价，主要用于所有医疗、医保、医药相关的满意度测评，本平台将涉及到多张满意度测评的表格，表格的数据主要“满意，非常满意”等单项选择题及少量的文本录入项"
      },
      {
        "id": "exuntong-button-00002",
        "cat": "button",
        "name": "健康档案",
        "iconClass_s": "icon-electronic",
        "pageUrl_s": "pages/residentfile/residentfile",
        "content":  "健康档案，指居民身心健康（正常的健康状况、亚健康的疾病预防健康保护促进、非健康的疾病治疗等）过程的规范、科学记录。是以居民个人健康为核心、贯穿整个生命过程、涵盖各种健康相关因素、实现信息多渠道动态收集、满足居民自身需要和健康管理的信息资源。以问题为导向的健康档案记录方式（problem oriented medical record ,POMR）是1968年由美国的Weed等首先提出来的，要求医生在医疗服务中采用以个体健康问题为导向的记录方式。目前已成为世界上许多国家和地区建立居民健康档案的基本方法"
      },
      {
        "id": "exuntong-button-00003",
        "cat": "button",
        "name": "慢病管理",
        "iconClass_s": "icon-disease",
        "pageUrl_s": "pages/disease/disease",
        "content":  "慢性疾病管理系统是一种为综合性医院及专科医院开发设计的慢性疾病管理网络系统。它全面导入疾病管理的概念，针对常见慢性病的诊疗与科研，帮助科室快速实现慢性病病历的系统管理，辅助医生护士的日常诊疗护理工作，并为医院向患者提供多样化诊疗服务创造条件,它包括高血压、心脏病、糖尿病、慢性肾功能衰竭、慢性病毒性肝炎、肝硬化、中风后遗症、恶性肿瘤、慢性肾小球肾炎、癫痫、帕金森综合症、肺结核、类风湿关节炎、系统性红疮狼斑、甲状腺或海洋性贫血、慢性再升障碍性贫血、血友病、器官移植术后、白内障、泌尿结石"
      },
      {
        "id": "exuntong-button-00004",
        "cat": "button",
        "name": "智能诊断",
        "iconClass_s": "icon-e-ai",
        "pageUrl_s": "pages/eai/eai",
        "content":  "上传您的医疗影像，智能诊断出您的病情,目前包括x光胸片智能诊断"
      },
      {
        "id": "exuntong-button-00005",
        "cat": "button",
        "name": "医保咨询",
        "iconClass_s": "icon-e-information",
        "pageUrl_s": "pages/information/information",
        "content":  "及时发布各种政策医疗咨询"
      }
    ]
    solrXml = SolrXml()
    solrXml.parse(objs)
    f = open('document/button-docs.xml','w')
    solrXml.mdoc.writexml(f,'','\t','\n','utf-8')
    f.close()

