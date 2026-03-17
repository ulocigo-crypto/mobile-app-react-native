import { Route, RouteComponentProps } from '@react-navigation/native';

type NavigationParams = {
  HomeScreen: undefined;
  DetailsScreen: {
    id: string;
    username: string;
    avatar_url: string;
  };
};

type HomeScreenProps = RouteComponentProps<NavigationParams['HomeScreen']>;

type DetailsScreenProps = RouteComponentProps<NavigationParams['DetailsScreen']>;