/*
All of the code within the ZingChart software is developed and copyrighted by PINT, Inc., and may not be copied,
replicated, or used in any other software or application without prior permission from PINT. All usage must coincide with the
ZingChart End User License Agreement which can be requested by email at support@zingchart.com.

Build 0.120731
*/
ZC.QU.push("maps");if(!zingchart.maps){zingchart.maps={};zingchart.maps.maps={};zingchart.maps.data={}}zingchart.maps.FORCESCALE=0;zingchart.maps.getInfo=function(d){var h=zingchart.maps.maps[d];h||(h=eval("zingchart.maps.data."+d));if(h)return h._INFO_||h;return null};
zingchart.maps.getItems=function(d){var h=zingchart.maps.maps[d];h||(h=eval("zingchart.maps.data."+d));if(h){d=[];for(var e in h)if(e!="_DEFAULTS_"&&e!="_INFO_"&&e!="_GROUPS_")if(h._INFO_)ZC.AH(h._INFO_.items,e)!=-1&&d.push(e);else d.push(e);return d}return null};
zingchart.maps.getItemInfo=function(d,h){var e,b;if(e=zingchart.maps.maps[d]){if(b=e[h]){zingchart.maps.lonlat2xy(e._INFO_.x,e._INFO_.y,e._INFO_.width,e._INFO_.height,[b.bbox[0]+(b.bbox[2]-b.bbox[0])/2,b.bbox[1]+(b.bbox[3]-b.bbox[1])/2],e._INFO_.bbox);return b}}else if((e=eval("zingchart.maps.data."+d))&&(b=e[h]))return b;return null};
zingchart.maps.getXY=function(d,h){var e;if(e=zingchart.maps.maps[d])return zingchart.maps.lonlat2xy(e._INFO_.x,e._INFO_.y,e._INFO_.width,e._INFO_.height,h,e._INFO_.bbox);return null};zingchart.maps.getLonLat=function(d,h){var e;if(e=zingchart.maps.maps[d])return zingchart.maps.xy2lonlat(e._INFO_.x,e._INFO_.y,e._INFO_.width,e._INFO_.height,h,e._INFO_.bbox);return null};
zingchart.maps.lonlat2xy=function(d,h,e,b,i,g){var n=e/ZC._a_(g[2]-g[0]);e=b/ZC._a_(g[3]-g[1]);d=d+(ZC._f_(i[0])-ZC.CT(g[0],g[2]))*n;h=h+b-(ZC._f_(i[1])-ZC.CT(g[1],g[3]))*e;return[d,h]};zingchart.maps.xy2lonlat=function(d,h,e,b,i,g){e=e/ZC._a_(g[2]-g[0]);b=b/ZC._a_(g[3]-g[1]);return[g[0]+(i[0]-d)/e,g[1]+(h-i[1])/b]};
zingchart.maps.mappoints=function(d,h,e,b,i,g){e=e/ZC._a_(i[2]-i[0]);var n=b/ZC._a_(i[3]-i[1]),f=[],o,p,k,l;p=d+(ZC.CT(g.bbox[0],g.bbox[2])-ZC.CT(i[0],i[2]))*e;k=h+b-(ZC.CT(g.bbox[1],g.bbox[3])-ZC.CT(i[1],i[3]))*n;ZC._a_(g.bbox[2]-g.bbox[0]);l=Math.abs(g.bbox[3]-g.bbox[1])*n;for(var c=0,a=g.coords.length;c<a;c++)if(g.coords[c]==null)f.push(null);else{b=d+(g.coords[c][0]-ZC.CT(i[0],i[2]))*e+g.transform.offsetLon*e;o=h+(ZC.BR(i[1],i[3])-g.coords[c][1])*n-g.transform.offsetLat*n;if(g.transform.scale!=
1){b=p+(b-p)*g.transform.scale;o=k-l+(o-(k-l))*g.transform.scale}f.push([ZC._i_(b),ZC._i_(o)])}return f};zingchart.maps.translate=function(d,h,e,b,i){e=e/ZC._a_(i[2]-i[0]);b=b/ZC._a_(i[3]-i[1]);return d=="x"?h*e:h*b};
zingchart.maps.convert=function(d){var h=d.data.options||{},e=d.id,b=d.groups,i=d.items,g=d.ignore,n=d.bbox,f=d.loader.A0A(d.loaderdata,d.graphid),o=ZC.ND(d.x);o=ZC._i_(o<1?f.plotarea.x+o*f.plotarea.width:o);var p=ZC.ND(d.y);p=ZC._i_(p<1?f.plotarea.y+p*f.plotarea.height:p);var k=ZC.ND(d.width);k=ZC._i_(k<=1?k*f.plotarea.width:k);var l=ZC.ND(d.height);l=ZC._i_(l<=1?l*f.plotarea.height:l);f={};ZC._cp_(d.map,f);if(k==0||l==0||!f)return[];var c,a;for(a in f)if(!(a=="_DEFAULTS_"||a=="_INFO_"||a=="_GROUPS_")){c=
[ZC.MAX,-ZC.MAX,-ZC.MAX,ZC.MAX];for(var j=0;j<f[a].coords.length;j++)if(f[a].coords[j]!=null){c[0]=ZC.CT(c[0],f[a].coords[j][0]+f[a].transform.offsetLon);c[1]=ZC.BR(c[1],f[a].coords[j][1]+f[a].transform.offsetLat);c[2]=ZC.BR(c[2],f[a].coords[j][0]+f[a].transform.offsetLon);c[3]=ZC.CT(c[3],f[a].coords[j][1]+f[a].transform.offsetLat)}if(f[a].transform.scale!=1){c[2]=c[0]+(c[2]-c[0])*f[a].transform.scale;c[3]=c[1]-(c[1]-c[3])*f[a].transform.scale}var m=ZC.CT(1,ZC._a_(c[2]-c[0])/8);d=ZC.CT(1,ZC._a_(c[3]-
c[1])/8);c[0]-=m;c[1]+=d;c[2]+=m;c[3]-=d;c[0]=ZC.BR(c[0],-180);c[1]=ZC.CT(c[1],90);c[2]=ZC.CT(c[2],180);c[3]=ZC.BR(c[3],-90);f[a].bbox=c}c=[ZC.MAX,-ZC.MAX,-ZC.MAX,ZC.MAX];m=[];if(b.length>0&&f._GROUPS_){j=0;for(var s=b.length;j<s;j++)if(f._GROUPS_[b[j]])m=m.concat(f._GROUPS_[b[j]])}if(i.length>0){j=0;for(s=i.length;j<s;j++)ZC.AH(g,i[j])==-1&&m.push(i[j])}else for(a in f)if(f.hasOwnProperty(a))a=="_DEFAULTS_"||a=="_INFO_"||a=="_GROUPS_"||b.length==0&&ZC.AH(g,a)==-1&&m.push(a);for(j=m.length-1;j>=0;j--)if(m[j]&&
m[j].indexOf("@")!=-1){a=m[j].split("@");ZC.AH(m,a[0])!=-1&&m.splice(j,1)}if(n!=null&&n.length==4)c=n;else{j=0;for(s=m.length;j<s;j++){a=m[j];if(f[a]){c[0]=ZC.CT(c[0],f[a].bbox[0]);c[1]=ZC.BR(c[1],f[a].bbox[1]);c[2]=ZC.BR(c[2],f[a].bbox[2]);c[3]=ZC.CT(c[3],f[a].bbox[3])}}}n=k/ZC._a_(c[2]-c[0]);i=l/ZC._a_(c[3]-c[1]);if(ZC._b_(h.scale)){a=1.4*n/i;if(a>1.05){a=ZC._i_(k/a);o+=(k-a)/2;k=a}else if(a<0.95){a=ZC._i_(l*a);p+=(l-a)/2;l=a}n=k/ZC._a_(c[2]-c[0]);i=l/ZC._a_(c[3]-c[1])}f._INFO_={x:o,y:p,width:k,
height:l,id:e,bbox:c,groups:b,items:m,ignore:g};zingchart.maps.maps[e]=f;b={};j=0;for(s=m.length;j<s;j++){a=m[j];if(f[a]){b[a]={type:"poly",id:a,points:zingchart.maps.mappoints(o,p,k,l,c,f[a]),label:{map:e},zSort:10,tooltip:{},connector:{}};for(var u=g=0,t=0,q,r=0,v=b[a].points.length;r<v-1;r++)if((d=b[a].points[r])!=null&&(q=b[a].points[r+1])!=null)t+=d[0]*q[1]-q[0]*d[1];t*=0.5;r=0;for(v=b[a].points.length;r<v-1;r++)if((d=b[a].points[r])!=null&&(q=b[a].points[r+1])!=null){g+=(d[0]+q[0])*(d[0]*q[1]-
q[0]*d[1]);u+=(d[1]+q[1])*(d[0]*q[1]-q[0]*d[1])}g/=6*t;u/=6*t;f[a].cpoint=[g,u];f._DEFAULTS_&&ZC._cp_(f._DEFAULTS_,b[a]);f[a].style&&ZC._cp_(f[a].style,b[a]);ZC._todash_(b[a]);ZC._cp_(h.style,b[a]);ZC._cp_(f[a].tooltip,b[a].tooltip);ZC._cp_(f[a].label,b[a].label);ZC._cp_(f[a].connector,b[a].connector);h.style!=null&&h.style.items!=null&&ZC._cp_(h.style.items[a],b[a]);if(b[a].connector.points!=null){d=0;for(t=b[a].connector.points.length;d<t;d++)b[a].connector.points[d]=zingchart.maps.lonlat2xy(o,
p,k,l,b[a].connector.points[d],c)}if(b[a].label.x==null)b[a].label.x=g;if(b[a].label.y==null)b[a].label.y=u}}a=1.4*n/i;if(!zingchart.maps.FORCESCALE&&(a>1.05||a<0.95))b._ALERT_={type:"circle",id:"_ALERT_",x:o+10,y:p+10,size:8,backgroundColor:"#c00",label:{color:"#fff",bold:true,text:"!"},tooltip:{text:"Scaling Error<br/>Use "+k+"/"+ZC._i_(l*a)+" or "+ZC._i_(k/a)+"/"+l,backgroundColor:"#c00",borderRadius:8,color:"#fff"}};return b};
