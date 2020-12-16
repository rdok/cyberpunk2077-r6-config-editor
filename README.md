# cybepunk2077

User Input Mappings

```
"${CYBERPUNK_2077_INSTALLATION_PATH}\r6\config\inputUserMappings.xml"
```

### Hold capslock to move
##### Forward / Back
```
<mapping name="LeftY_Axis" type="Axis" >
  ...
  <button id="IK_W" val="1.0" overridableUI="forward"/>
  <button id="IK_CapsLock" val="0" overridableUI="forward"/>
  
  <button id="IK_S" val="-1.0" overridableUI="back"/>
  <button id="IK_CapsLock" val="0" overridableUI="back"/>
  ...
</mapping>
```

##### Left / Right
```
<mapping name="LeftX_Axis" type="Axis" >
  ...
  <button id="IK_A" val="-1.0" overridableUI="left"/>
  <button id="IK_CapsLock" val="0" overridableUI="left"/>

  <button id="IK_D" val="1.0" overridableUI="right"/>
  <button id="IK_CapsLock" val="0" overridableUI="right"/>
  ...
</mapping>
```
