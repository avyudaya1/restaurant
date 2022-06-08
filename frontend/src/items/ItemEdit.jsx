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
} from 'react-admin';

const ItemEdit = () => (
    <Edit>
        <SimpleForm>
            {/* <ReferenceInput source="userId" reference="users">
                <SelectInput optionText="id" />
            </ReferenceInput> */}
            <TextInput source="name" />
            <SelectInput source="unit" choices={[
                {
                    id: "Kilogram",
                    name: "Kilogram"
                },
                {
                    id: "Litre",
                    name: "Litre"
                }
            ]}/>
            <NumberInput source="quantity"/>
            <DateInput source="manufacture_date"/>
            <DateInput source="expiry_date"/>
            <NumberInput source="price"/>
        </SimpleForm>
    </Edit>
);

export default ItemEdit;