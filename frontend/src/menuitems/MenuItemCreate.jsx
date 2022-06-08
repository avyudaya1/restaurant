import * as React from "react";
import {
  List,
  Datagrid,
  TextField,
  ReferenceField,
  EditButton,
  Edit,
  SimpleForm,
  ReferenceInput,
  SelectInput,
  NumberInput,
  TextInput,
  DateInput,
  Create,
} from "react-admin";

const MenuItemCreate = () => (
  <Create>
    <SimpleForm>
        <TextInput source="name" />
        <TextInput source="ingredients" />
        <TextInput source="cooking_time" />
        <NumberInput source="cost" />
        <TextInput source="menu_category" />
    </SimpleForm>
  </Create>
);

export default MenuItemCreate;
