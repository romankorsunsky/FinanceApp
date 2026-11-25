import { NewsItemProps } from "@/Types/Types";
import { Dimensions, Text, View } from "react-native";

const screenWidth = Dimensions.get("screen").width;
export default function NewsItemComponent({title,content}:NewsItemProps){
    return (
    <View style={{
        padding:2,
        marginTop: 10,
        marginBottom: 10,
        borderRadius: 8,
        width: screenWidth - 20,
        backgroundColor: "#1c1c1c"}}>
        <View>
            <Text style={{fontWeight: "bold",color: "white"}}>
                {title}
            </Text>
        </View>
        <View style={{backgroundColor: "#91ff94",borderRadius: 8}}>
            <Text>
                {content}
        </Text>
        </View>
    </View>);
}