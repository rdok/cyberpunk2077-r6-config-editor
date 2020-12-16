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
  <button id="IK_CapsLock" val="0" overridableUI="slowWalk"/>
  ...
</mapping>
```

##### Left / Right
```
<mapping name="LeftX_Axis" type="Axis" >
  ...
  <button id="IK_CapsLock" val="0" overridableUI="slowWalk"/>
  ...
</mapping>
```

### Enable additional keymaps
Use case: view & edit keymap for quickly opening the consumables inventory. 
```
<context name="SettingsUI">
  ...
  <include name="UIExploration" />
  <include name="UIShared" />
  <include name="UIMenu" />
  ...
</context>
```

### Performance tweaks
Setup https://github.com/yamashi/PerformanceOverhaulCyberpunk/wiki
