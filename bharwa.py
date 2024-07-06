# Import Spark NLP
from sparknlp.base import *
from sparknlp.annotator import *
from sparknlp.pretrained import PretrainedPipeline
import sparknlp

text = ["میرے وکلاء کی ٹیم نےفصیح الدین کی قیادت میں امریکہ میں جیو اور میرشکیل کیخلاف ڈیمانڈ نوٹس دائر کردیا ہے۔ جیو اور اس کے سرپرستوں کیجانب سے جھوٹی خبروں اور غلط معلومات کےفروغ کےکلچر سےعدالتوں میں نمٹا جائے گا۔"]

#lang_pipe  = sparknlp.load('xx.ur.translate_to.en').predict(text, output_level='sentence')
#lang_pipe

spark = sparknlp.start()
pipeline = PretrainedPipeline('xx.ur.translate_to.en',)
result = pipeline.predict(text)
list(result.keys())
