void setup() {
  Serial.begin(9600);
}
String data;
char list[20][20];
int index,listindex,i,j;
int l;
void loop() {
  if(Serial.available()){
    for(i=0;i<20;i++){
      for(j=0;j<20;j++){
        list[i][j]='\0';
      }
    }
    data=Serial.readStringUntil('\n');
    l=data.length();
    index=-1;
    listindex=0;
    for(i=0;i<l;i++){
      if(data[i]=='#'){
        int jindex=0;
        for(j=index+1;j<i;j++){
          list[listindex][jindex++]=data[j];
        }
        listindex++;
        index=i;
      }
      if(i==(l-1)){
        if(data[i]!='#'){
          int jindex=0;
          for(j=index+1;j<l;j++){
            list[listindex][jindex++]=data[j];
          }
          listindex++;
        }
      }
    }
    for(i=0;i<listindex;i++){
      Serial.println(list[i]);
    }
    
  }
  delay(50);
}
