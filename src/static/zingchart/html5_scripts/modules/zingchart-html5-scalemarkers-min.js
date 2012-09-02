/*
All of the code within the ZingChart software is developed and copyrighted by PINT, Inc., and may not be copied,
replicated, or used in any other software or application without prior permission from PINT. All usage must coincide with the
ZingChart End User License Agreement which can be requested by email at support@zingchart.com.

Build 0.120731
*/
ZC.QU.push("scalemarkers");
ZC.Y2=ZC.CY.B6({$i:function(a){this.b(a);this.AB=0.25;this.J=0;this.FF=this.K=this.AC=null;this.VV=0;this.CB="bottom"},parse:function(){var a;this.b();this.Q4_a([["type","AC"],["value-range","VV","b"],[ZC._[9],"CB"],["range","FF"]]);if((a=this.o.label)!=null||this.o.text!=null){this.K=new ZC.D1(this);this.A.A.A.AR.load(this.K.o,["("+this.A.AC+").SCALE.marker.label"]);this.o.text!=null&&this.K.append({text:this.o.text});this.K.append(a);this.K.parse()}},paint:function(){var a=this;if(a.AM){var b=a.A,
l=b.A.P+"-scales-"+(a.CB=="top"?"f":"b")+"l-0-c",f=ZC.L.CN(b.H.usc()?b.H.P+"-main-c":l,b.H.A5),c,d,g,h,e=[],j=0,k=0;if(b.CV)j=b.EP?k=(b.AF?-1:1)*b.V/2:k=-b.V/2;if(a.K!=null){a.K.X=b.H.usc()?b.H.mc():ZC.AN(b.A.P+"-scales-ml-0-c");a.K.P=a.A.P+"-marker-label-"+a.J;a.K.F1=a.A.P+"-marker-label "+a.A.A.P+"-scale-marker-label zc-scale-marker-label"}var i=function(m,n){return a.VV?m.B8(n):m.MG(n)};if(a.AC=="line"){if(b.BH.indexOf(ZC._[52])!=-1)if(a.FF.length==1)c=d=i(b,a.FF[0])+j;else{if(a.FF.length==2){c=
i(b,a.FF[0])+j;d=i(b,a.FF[1])+j}}else if(b.BH.indexOf(ZC._[53])!=-1)if(a.FF.length==1)c=d=b.B8(a.FF[0]);else if(a.FF.length==2){c=b.B8(a.FF[0]);d=b.B8(a.FF[1])}if(b.BH.indexOf(ZC._[52])!=-1&&b.EP||b.BH.indexOf(ZC._[53])!=-1&&!b.EP){e.push([b.iX,c],[b.iX+b.G,d]);if(a.K!=null){a.K.iX=b.iX;a.K.iY=c-(b.AF?0:a.K.E)}}else{e.push([c,b.iY+b.E],[d,b.iY]);if(a.K!=null){a.K.iX=c-(b.AF?a.K.G:0);a.K.iY=b.iY+b.E-a.K.E}}if(b.A.AQ["3d"]){b.A.JC();c=0;for(d=e.length;c<d;c++){g=new ZC.C0(b.A,e[c][0]-ZC.AK.DZ,e[c][1]-
ZC.AK.DY,ZC.AK.FS);e[c][0]=g.DD[0];e[c][1]=g.DD[1]}}if(e.length==2){ZC.BW.setup(f,a);ZC.BW.paint(f,a,e)}}else if(a.AC=="area"){if(b.BH.indexOf(ZC._[52])!=-1)if(a.FF.length==2){c=g=i(b,a.FF[0])+j;d=h=i(b,a.FF[1])+k}else{if(a.FF.length==4){c=i(b,a.FF[0])+j;d=i(b,a.FF[1])+k;g=i(b,a.FF[2])+j;h=i(b,a.FF[3])+k}}else if(b.BH.indexOf(ZC._[53])!=-1)if(a.FF.length==2){c=g=b.B8(a.FF[0]);d=h=b.B8(a.FF[1])}else if(a.FF.length==4){c=b.B8(a.FF[0]);d=b.B8(a.FF[1]);g=b.B8(a.FF[2]);h=b.B8(a.FF[3])}d=c==d?d+1:d;h=g==
h?h+1:h;if(b.BH.indexOf(ZC._[52])!=-1&&b.EP||b.BH.indexOf(ZC._[53])!=-1&&!b.EP){e.push([b.iX,c],[b.iX+b.G,g],[b.iX+b.G,h],[b.iX,d],[b.iX,c]);if(a.K!=null){a.K.iX=b.iX;a.K.iY=c-(b.AF?0:a.K.E)}}else{e.push([c,b.iY+b.E],[g,b.iY],[h,b.iY],[d,b.iY+b.E],[c,b.iY+b.E]);if(a.K!=null){a.K.iX=c-(b.AF?a.K.G:0);a.K.iY=b.iY+b.E-a.K.E}}if(e.length>=4){if(b.A.AQ["3d"]){b.A.JC();c=0;for(d=e.length;c<d;c++){g=new ZC.C0(b.A,e[c][0]-ZC.AK.DZ,e[c][1]-ZC.AK.DY,ZC.AK.FS);e[c][0]=g.DD[0];e[c][1]=g.DD[1]}}f=new ZC.CY(a.A);
f.P=b.P+"-marker-"+a.J;f.X=b.H.usc()?b.H.mc():ZC.AN(l);f.copy(a);f.AG=0;f.AE=0;f.EN=0;f.G2=0;f.C=e;f.parse();f.paint()}}if(a.K!=null){if(b.BH.indexOf(ZC._[52])!=-1&&!b.EP||b.BH.indexOf(ZC._[53])!=-1&&b.EP)if(a.K.o.angle==null)a.K.A7=270;if(a.K.A7%180==90)if(b.BH.indexOf(ZC._[52])!=-1)if(b.EP){a.K.C9-=a.K.G/2-a.K.E/2;a.K.CF-=(b.AF?-1:1)*(a.K.G/2-a.K.E/2)}else{a.K.C9-=(b.AF?-1:1)*(a.K.G/2-a.K.E/2);a.K.CF-=a.K.G/2-a.K.E/2}else if(b.BH.indexOf(ZC._[53])!=-1)if(b.EP){a.K.C9-=(b.AF?-1:1)*(a.K.G/2-a.K.E/
2);a.K.CF-=a.K.G/2-a.K.E/2}else{a.K.C9-=a.K.G/2-a.K.E/2;a.K.CF-=(b.AF?-1:1)*(a.K.G/2-a.K.E/2)}a.K.paint();a.K.D7()}}}});