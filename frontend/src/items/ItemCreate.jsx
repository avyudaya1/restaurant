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

const ItemCreate = () => (
  <Create>
    <SimpleForm>
      <TextInput source="name" />
      <SelectInput
        source="unit"
        choices={[
          {
            id: "Kilogram",
            name: "Kilogram",
          },
          {
            id: "Litre",
            name: "Litre",
          },
        ]}
      />
      <NumberInput source="quantity" />
      <DateInput source="manufacture_date" />
      <DateInput source="expiry_date" />
      <NumberInput source="price" />
    </SimpleForm>
  </Create>
);

export default ItemCreate;
